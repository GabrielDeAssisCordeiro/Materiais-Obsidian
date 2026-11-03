---
titulo: "C++ em sistemas operacionais e infraestrutura"
tags: [cpp, aplicacoes, posix, drivers]
aliases: ["Programação de sistemas", "Sistemas operacionais", "POSIX", "syscalls", "Drivers", "Daemons", "Infraestrutura"]
tipo: area
nivel: avancado
padrao: C++17
criado: 2026-10-24
relacionados: ["[[RAII]]", "[[Deleters Customizados]]", "[[Códigos de Erro e error_code]]"]
---

# C++ em sistemas operacionais e infraestrutura

C++ é usado em **componentes de sistema**: partes de SOs (Windows, macOS/iOS/Android/Fuchsia), *drivers*, sistemas de arquivos, hypervisors, bancos de dados, *runtimes*, servidores de alto desempenho (nginx é C; envoy, ScyllaDB, Redpanda e outros usam C++).

| Contexto | Observação |
|---|---|
| **Espaço de usuário** | POSIX/Win32: processos, arquivos, sockets, `epoll`/`io_uring`/IOCP |
| **Kernel Linux** | C (e Rust); C++ geralmente **não** é usado no kernel |
| **Windows kernel/drivers** | C/C++ restrito (WDK, sem exceções/RTTI padrão) |
| **Hypervisors / firmware** | C++ freestanding, *no-std* |
| **Daemons e serviços** | systemd units, sinais, logs, *graceful shutdown* |

## RAII sobre APIs do sistema

Descritores de arquivo, *handles* e mapeamentos de memória são recursos clássicos: embrulhe em RAII ([[RAII]], [[Deleters Customizados]]).

```cpp
// g++ -std=c++20 -Wall -Wextra
// (exemplo para Linux/POSIX)
#include <cerrno>
#include <cstring>
#include <fcntl.h>
#include <iostream>
#include <system_error>
#include <unistd.h>
#include <utility>

class Fd {
public:
    explicit Fd(int fd = -1) noexcept : fd_{fd} {}
    ~Fd() { if (fd_ >= 0) ::close(fd_); }
    Fd(const Fd&) = delete;
    Fd& operator=(const Fd&) = delete;
    Fd(Fd&& o) noexcept : fd_{std::exchange(o.fd_, -1)} {}
    Fd& operator=(Fd&& o) noexcept { Fd tmp{std::move(o)}; std::swap(fd_, tmp.fd_); return *this; }
    int get() const noexcept { return fd_; }
    explicit operator bool() const noexcept { return fd_ >= 0; }
private:
    int fd_;
};

Fd abrir(const char* caminho, int flags) {
    Fd fd{::open(caminho, flags)};
    if (!fd) throw std::system_error{errno, std::generic_category(), caminho};   // erro do SO → exceção
    return fd;
}

int main() {
    try {
        Fd f = abrir("/etc/hostname", O_RDONLY);
        char buf[128];
        ssize_t n = ::read(f.get(), buf, sizeof buf - 1);
        if (n > 0) { buf[n] = '\0'; std::cout << buf; }
        Fd inexistente = abrir("/nao/existe", O_RDONLY);
    } catch (const std::system_error& e) {
        std::cout << "erro: " << e.code().message() << '\n';
    }
}
```

## Técnicas e práticas

- **I/O assíncrono**: `epoll` (Linux), `kqueue` (BSD/macOS), IOCP (Windows), `io_uring`; abstraídas por [[Asio e Rede]].
- **Memória**: `mmap`, *huge pages*, alocadores NUMA-conscientes ([[Alocadores Introdução]]).
- **Concorrência**: afinidade de CPU, `futex`, filas lock-free ([[Atomics e Modelo de Memória]]).
- **Sinais**: trate apenas funções *async-signal-safe* dentro do manipulador; use *self-pipe* ou `signalfd`.
- **Observabilidade**: logs estruturados, métricas, *tracing* (OpenTelemetry), `perf`, `eBPF`.
- **Segurança**: *sandboxing* (seccomp), privilégios mínimos, ASLR, `-fstack-protector`, `_FORTIFY_SOURCE` ([[Segurança e Hardening]]).

> [!warning] Portabilidade
> Código POSIX não compila no Windows e vice-versa: isole detalhes em uma **camada de plataforma** (ou use [[Asio e Rede]], [[Poco]], [[std filesystem]]).

## Veja também

- [[RAII]]
- [[Deleters Customizados]]
- [[Códigos de Erro e error_code]]
- [[Segurança e Hardening]]
- [[MOC - Áreas de Aplicação - Cpp]]

## Exercício

1. Estenda `Fd` com `lido(buffer)` e `escrito(buffer)` que tratam `EINTR`.
2. Escreva um *daemon* simples que reinicia a configuração ao receber `SIGHUP`.
