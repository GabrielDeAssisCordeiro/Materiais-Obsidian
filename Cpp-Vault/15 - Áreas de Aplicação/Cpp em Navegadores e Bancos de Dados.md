---
titulo: "C++ em navegadores e bancos de dados"
tags: [cpp, aplicacoes, sqlite]
aliases: ["Navegadores", "Chromium", "Firefox", "Bancos de dados", "RocksDB", "ClickHouse", "MySQL", "LRU", "Motores de busca"]
tipo: area
nivel: avancado
padrao: C++20
criado: 2026-10-24
relacionados: ["[[Cpp em Sistemas Operacionais e Infraestrutura]]", "[[map e set]]", "[[Segurança e Hardening]]"]
---

# C++ em navegadores e bancos de dados

## Navegadores

**Chromium/Chrome/Edge** (Blink, V8 em C++), **Firefox** (Gecko — C++ e Rust), **WebKit/Safari** são grandes bases C++. Desafios típicos:

| Tema | Detalhe |
|---|---|
| Segurança | Grande parte das vulnerabilidades críticas é de **memória** (use-after-free, estouro). Mitigações: sandbox multiprocesso, `MiraclePtr`/`raw_ptr`, *hardened allocators*, adoção de Rust em partes novas |
| Desempenho | Compilação JIT (V8), layout, renderização acelerada por GPU (Skia) |
| Escala | Milhões de linhas, milhares de contribuidores: *style guides* rígidos (Chromium/Google C++ Style), monorepo, *code review*, CI pesada |
| Isolamento | Processo por *site*, IPC com Mojo |

## Bancos de dados e armazenamento

C++ é comum em **motores de banco**: MySQL, MongoDB, ClickHouse, ScyllaDB, RocksDB/LevelDB, DuckDB, parte do SQLite (C), Apache Arrow, Velox.

| Componente | Técnicas |
|---|---|
| **Buffer pool / cache** | LRU/CLOCK, alocadores próprios |
| **Índices** | B-tree, LSM-tree, *skip lists*, hash |
| **Execução** | Vetorizada (SIMD), compilação JIT de consultas |
| **Armazenamento** | WAL (*write-ahead log*), `mmap`, `O_DIRECT`, `io_uring` |
| **Concorrência** | MVCC, locks de granularidade fina, estruturas lock-free |
| **Layout colunar** | Melhor uso de cache e compressão |

## Exemplo: cache LRU

```cpp
// g++ -std=c++20 -Wall -Wextra
#include <iostream>
#include <list>
#include <optional>
#include <string>
#include <unordered_map>
#include <utility>

template <typename K, typename V>
class CacheLRU {
public:
    explicit CacheLRU(std::size_t capacidade) : cap_{capacidade} {}

    std::optional<V> obter(const K& k) {
        auto it = indice_.find(k);
        if (it == indice_.end()) return std::nullopt;
        itens_.splice(itens_.begin(), itens_, it->second);           // move para a frente: O(1)
        return it->second->second;
    }

    void inserir(const K& k, V v) {
        if (auto it = indice_.find(k); it != indice_.end()) {
            it->second->second = std::move(v);
            itens_.splice(itens_.begin(), itens_, it->second);
            return;
        }
        if (itens_.size() == cap_) {                                 // remove o menos recente
            indice_.erase(itens_.back().first);
            itens_.pop_back();
        }
        itens_.emplace_front(k, std::move(v));
        indice_[k] = itens_.begin();
    }

private:
    std::size_t cap_;
    std::list<std::pair<K, V>> itens_;                               // ordem de uso
    std::unordered_map<K, typename std::list<std::pair<K, V>>::iterator> indice_;
};

int main() {
    CacheLRU<std::string, int> c{2};
    c.inserir("a", 1);
    c.inserir("b", 2);
    c.obter("a");                                                    // "a" fica recente
    c.inserir("c", 3);                                               // expulsa "b"
    std::cout << c.obter("a").value_or(-1) << c.obter("b").value_or(-1) << c.obter("c").value_or(-1) << '\n';   // 1-13
}
```

> [!info] Por que a lista guarda iteradores
> `std::list::splice` **não invalida iteradores** ([[Complexidade e Invalidação de Iteradores]]), permitindo guardar iteradores no `unordered_map` e reordenar em O(1).

> [!danger] Segurança de memória
> Parsers de HTML/imagem/vídeo e protocolos de banco processam **entrada não confiável**: [[Fuzzing]], [[Sanitizers]] e [[Segurança e Hardening]] são essenciais.

## Veja também

- [[Cpp em Sistemas Operacionais e Infraestrutura]]
- [[map e set]]
- [[Fuzzing]]
- [[Segurança e Hardening]]
- [[MOC - Áreas de Aplicação - Cpp]]

## Exercício

1. Torne o `CacheLRU` thread-safe com `std::shared_mutex` e discuta a contenção.
2. Implemente uma pequena *skip list* e compare com `std::map` em inserções e buscas.
