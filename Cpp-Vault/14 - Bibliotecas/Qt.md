---
titulo: "Qt"
tags: [cpp, bibliotecas]
aliases: ["Qt", "Qt 6", "QML", "Qt Widgets", "signals e slots", "Qt Creator"]
tipo: biblioteca
nivel: intermediario
padrao: C++17
criado: 2026-10-24
relacionados: ["[[Visão Geral das Bibliotecas]]", "[[CMake Moderno e Presets]]", "[[Herança]]"]
---

# Qt

*Framework* multiplataforma para **GUI e aplicações** (desktop, embarcado, mobile): widgets, QML (UI declarativa), rede, SQL, multimídia, concorrência, XML/JSON, internacionalização. Licenças: **LGPL/GPL** (open source, com obrigações — em especial para linkagem estática) e comercial.

| Conceito | Descrição |
|---|---|
| `QObject` | Base de objetos com **sinais/slots**, propriedades e árvore pai/filho (o pai destrói os filhos) |
| **Signals & slots** | Comunicação desacoplada entre objetos |
| **moc** (*Meta-Object Compiler*) | Gera código para a macro `Q_OBJECT` |
| **Qt Widgets** | UI clássica de desktop |
| **QML / Qt Quick** | UI declarativa com GPU, ligada a C++ |
| `QString`, `QList`, `QVariant` | Tipos próprios (Unicode, *implicit sharing*) |
| `QThread`, `QtConcurrent`, `QFuture` | Concorrência |

```cpp
// [nv] g++ -std=c++20 -fPIC $(pkg-config --cflags --libs Qt6Widgets)   (requer Qt 6; indisponível no ambiente de teste do vault; use CMake no projeto real)
#include <QApplication>
#include <QPushButton>
#include <QLabel>
#include <QVBoxLayout>
#include <QWidget>

int main(int argc, char* argv[]) {
    QApplication app{argc, argv};

    QWidget janela;
    auto* layout = new QVBoxLayout{&janela};            // 'new' sem delete: o pai (janela) assume a posse
    auto* rotulo = new QLabel{"Cliques: 0"};
    auto* botao = new QPushButton{"Clique"};
    layout->addWidget(rotulo);
    layout->addWidget(botao);

    int cliques = 0;
    QObject::connect(botao, &QPushButton::clicked, [&] {   // signal → lambda
        rotulo->setText(QString("Cliques: %1").arg(++cliques));
    });

    janela.show();
    return app.exec();                                   // laço de eventos
}
```

```cmake
cmake_minimum_required(VERSION 3.21)
project(qtdemo LANGUAGES CXX)
set(CMAKE_AUTOMOC ON)                                    # roda o moc automaticamente
find_package(Qt6 REQUIRED COMPONENTS Widgets)
add_executable(app main.cpp)
target_link_libraries(app PRIVATE Qt6::Widgets)
```

> [!warning] Pontos de atenção
> - Qt tem **seu modelo de memória** (árvore de `QObject`): misturar com `unique_ptr`/`shared_ptr` exige cuidado ([[RAII]]).
> - Evite acessar a GUI fora da thread principal.
> - Verifique a **licença** antes de distribuir um produto fechado.
> - `signals`/`slots`/`emit` são macros: podem conflitar com outras bibliotecas (`QT_NO_KEYWORDS`).

> [!question] Verificar na documentação oficial
> Versão atual do Qt 6, módulos disponíveis e termos de licenciamento em qt.io.

## Veja também

- [[Visão Geral das Bibliotecas]]
- [[Herança]]
- [[Lambdas e Captura]]
- [[RAII]]

## Exercício

1. Faça uma calculadora simples com Qt Widgets.
2. Conecte um sinal a uma lambda e a um método e explique a diferença no ciclo de vida.
