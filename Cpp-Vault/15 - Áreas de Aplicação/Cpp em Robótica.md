---
titulo: "C++ em robótica"
tags: [cpp, aplicacoes]
aliases: ["Robótica", "ROS", "ROS 2", "Controle PID", "Tempo real", "Veículos autônomos", "Navigation2"]
tipo: area
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[OpenCV]]", "[[Eigen e Álgebra Linear]]", "[[Threads e jthread]]"]
---

# C++ em robótica

C++ é a linguagem principal para **controle em tempo real**, percepção e navegação em robôs e veículos autônomos. O ecossistema central é o **ROS 2** (*Robot Operating System*), um *middleware* de nós que se comunicam por tópicos, serviços e ações.

| Conceito ROS 2 | Descrição |
|---|---|
| **Nó** (`rclcpp::Node`) | Processo/componente com responsabilidade única |
| **Tópico** | Publicação/assinatura assíncrona (sensores, comandos) |
| **Serviço** | Requisição/resposta síncrona |
| **Ação** | Tarefa longa com *feedback* e cancelamento |
| **QoS** | Políticas de entrega (confiável, melhor esforço, histórico) |
| **DDS** | Camada de transporte (Fast DDS, Cyclone DDS) |
| **Pacotes** | `colcon build`, `ament_cmake` |
| Bibliotecas | **Eigen**, **OpenCV**, PCL (nuvens de pontos), MoveIt, Nav2, Orocos KDL |

```cpp
// [nv] g++ -std=c++17 -Wall -Wextra   (requer ROS 2 e rclcpp; compile com colcon; indisponível no ambiente de teste do vault)
#include <chrono>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

using namespace std::chrono_literals;

class Publicador : public rclcpp::Node {
public:
    Publicador() : Node("publicador"), contador_{0} {
        pub_ = create_publisher<std_msgs::msg::String>("chatter", 10);
        timer_ = create_wall_timer(500ms, [this] {
            std_msgs::msg::String msg;
            msg.data = "olá " + std::to_string(contador_++);
            pub_->publish(msg);
        });
    }
private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_;
    rclcpp::TimerBase::SharedPtr timer_;
    int contador_;
};

int main(int argc, char** argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Publicador>());
    rclcpp::shutdown();
}
```

## Controle PID (compilável)

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <algorithm>
#include <iostream>

class PID {
public:
    PID(double kp, double ki, double kd, double minimo, double maximo)
        : kp_{kp}, ki_{ki}, kd_{kd}, min_{minimo}, max_{maximo} {}

    double atualizar(double alvo, double medido, double dt) {
        const double erro = alvo - medido;
        integral_ = std::clamp(integral_ + erro * dt, min_, max_);       // anti-windup simples
        const double derivada = (erro - erro_anterior_) / dt;
        erro_anterior_ = erro;
        return std::clamp(kp_ * erro + ki_ * integral_ + kd_ * derivada, min_, max_);
    }
private:
    double kp_, ki_, kd_, min_, max_;
    double integral_ = 0.0, erro_anterior_ = 0.0;
};

int main() {
    PID pid{2.0, 0.5, 0.1, -10.0, 10.0};
    double posicao = 0.0;
    const double dt = 0.01;
    for (int i = 0; i < 1000; ++i) posicao += pid.atualizar(1.0, posicao, dt) * dt;   // planta simples: integrador
    std::cout << posicao << '\n';                                                       // próximo de 1
}
```

> [!warning] Tempo real
> - **Determinismo**: evite alocação dinâmica e exceções no laço de controle; use prioridades `SCHED_FIFO`, `PREEMPT_RT`, `mlockall`.
> - Cuidado com *callbacks* concorrentes em `MultiThreadedExecutor` (data races — [[Data Races e Deadlocks]]).
> - **Unidades e referenciais**: use tipos fortes (`std::chrono`, bibliotecas de unidades) para evitar erros graves.
> - Segurança funcional (ISO 26262, IEC 61508) exige processos e subconjuntos de linguagem (MISRA/AUTOSAR).

## Veja também

- [[OpenCV]]
- [[Eigen e Álgebra Linear]]
- [[Threads e jthread]]
- [[Cpp em Sistemas Embarcados]]
- [[MOC - Áreas de Aplicação - Cpp]]

## Exercício

1. Simule um motor com atraso de primeira ordem e ajuste os ganhos do PID.
2. Em ROS 2, escreva um nó assinante que filtre mensagens com média móvel.
