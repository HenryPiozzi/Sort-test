import time
import random
import statistics
import sys

sys.setrecursionlimit(500000)  # Necessário para vetores grandes

trocas_global = 0

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    global trocas_global
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    trocas_global += 1
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            trocas_global += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    trocas_global += 1
    return i + 1

def executar_testes(vetor_original, tamanho, repeticoes=3):
    global trocas_global
    tempos = []
    trocas_lista = []
    for r in range(repeticoes):
        arr = vetor_original.copy()
        trocas_global = 0
        inicio = time.perf_counter()
        quick_sort(arr, 0, len(arr) - 1)
        fim = time.perf_counter()
        elapsed = fim - inicio
        trocas = trocas_global
        tempos.append(elapsed)
        trocas_lista.append(trocas)
        print(f"  Execução {r+1}: {elapsed:.6f}s | Trocas: {trocas}")
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0
    print(f"  Tempo médio: {media:.6f}s")
    print(f"  Desvio padrão: {desvio:.6f}s")
    print(f"  Trocas (última execução): {trocas_lista[-1]}")
    return tempos, media, desvio, trocas_lista[-1]

def main():
    tamanhos = [1000, 10000, 100000]
    resultados = {}
    seeds = {1000: 42, 10000: 42, 100000: 42}
    print("quick sort O(n log n) médio / O(n²) pior caso")
    for tamanho in tamanhos:
        random.seed(seeds[tamanho])
        vetor = [random.randint(0, 10**9) for _ in range(tamanho)]
        print(f"\nTamanho do vetor: {tamanho}")
        tempos, media, desvio, trocas = executar_testes(vetor, tamanho)
        resultados[tamanho] = {
            "exec1": tempos[0],
            "exec2": tempos[1],
            "exec3": tempos[2],
            "media": media,
            "desvio": desvio,
            "trocas": trocas,
        }

    print("resumo")
    print(f"{'Tamanho':<12} {'Exec1(s)':<12} {'Exec2(s)':<12} {'Exec3(s)':<12} {'Média(s)':<12} {'Desvio(s)':<12} {'Trocas'}")
    for tamanho, r in resultados.items():
        print(f"{tamanho:<12} {r['exec1']:<12.6f} {r['exec2']:<12.6f} {r['exec3']:<12.6f} {r['media']:<12.6f} {r['desvio']:<12.6f} {r['trocas']}")

if __name__ == "__main__":
    main()
