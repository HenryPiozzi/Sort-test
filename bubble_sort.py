import time
import random
import statistics

def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
    return trocas

def executar_testes(vetor_original, tamanho, repeticoes=3):
    tempos = []
    trocas_lista = []

    for r in range(repeticoes):
        arr = vetor_original.copy()
        inicio = time.perf_counter()
        trocas = bubble_sort(arr)
        fim = time.perf_counter()
        elapsed = fim - inicio
        tempos.append(elapsed)
        trocas_lista.append(trocas)
        print(f"  Execução {r+1}: {elapsed:.6f}s | Trocas: {trocas}")

    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0

    print(f"  Tempo médio: {media:.6f}s")
    print(f"  Desvio padrão: {desvio:.6f}s")
    print(f"  Trocas (última execução): {trocas_lista[-1]}")
    print()

    return tempos, media, desvio, trocas_lista[-1]

def main():
    tamanhos = [1000, 10000, 100000]
    resultados = {}
    seeds = {1000: 42, 10000: 42, 100000: 42}

    print("bubble sort O(n²)")

    for tamanho in tamanhos:
        random.seed(seeds[tamanho])
        vetor = [random.randint(0, 10**9) for _ in range(tamanho)]

        print(f"tamanho do vetor: {tamanho}")
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
