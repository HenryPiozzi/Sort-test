import time
import random
import statistics

movimentacoes_global = 0

def merge_sort(arr):
    global movimentacoes_global
    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esq = merge_sort(arr[:meio])
    dir = merge_sort(arr[meio:])
    return merge(esq, dir)

def merge(esq, dir):
    global movimentacoes_global
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]:
            resultado.append(esq[i])
            i += 1
        else:
            resultado.append(dir[j])
            j += 1
        movimentacoes_global += 1 

    while i < len(esq):
        resultado.append(esq[i])
        i += 1
        movimentacoes_global += 1

    while j < len(dir):
        resultado.append(dir[j])
        j += 1
        movimentacoes_global += 1

    return resultado

def executar_testes(vetor_original, tamanho, repeticoes=3):
    global movimentacoes_global
    tempos = []
    movs_lista = []

    for r in range(repeticoes):
        arr = vetor_original.copy()
        movimentacoes_global = 0

        inicio = time.perf_counter()
        merge_sort(arr)
        fim = time.perf_counter()

        elapsed = fim - inicio
        movs = movimentacoes_global
        tempos.append(elapsed)
        movs_lista.append(movs)
        print(f"  Execução {r+1}: {elapsed:.6f}s | Movimentações: {movs}")

    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0

    print(f"  Tempo médio: {media:.6f}s")
    print(f"  Desvio padrão: {desvio:.6f}s")
    print(f"  Movimentações (última execução): {movs_lista[-1]}")
    print()

    return tempos, media, desvio, movs_lista[-1]

def main():
    tamanhos = [1000, 10000, 100000]
    resultados = {}
    seeds = {1000: 42, 10000: 42, 100000: 42}
    print("Merge sort O(n log n)")

    for tamanho in tamanhos:
        random.seed(seeds[tamanho])
        vetor = [random.randint(0, 10**9) for _ in range(tamanho)]
        print(f"\nTamanho do vetor: {tamanho}")
        tempos, media, desvio, movs = executar_testes(vetor, tamanho)
        resultados[tamanho] = {
            "exec1": tempos[0],
            "exec2": tempos[1],
            "exec3": tempos[2],
            "media": media,
            "desvio": desvio,
            "movimentacoes": movs,
        }
    print("resumo")
    print(f"{'Tamanho':<12} {'Exec1(s)':<12} {'Exec2(s)':<12} {'Exec3(s)':<12} {'Média(s)':<12} {'Desvio(s)':<12} {'Movimentações'}")
    for tamanho, r in resultados.items():
        print(f"{tamanho:<12} {r['exec1']:<12.6f} {r['exec2']:<12.6f} {r['exec3']:<12.6f} {r['media']:<12.6f} {r['desvio']:<12.6f} {r['movimentacoes']}")

if __name__ == "__main__":
    main()
