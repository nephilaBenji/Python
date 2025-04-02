def metros_e_cm_para_pes_e_polegadas(metros: float, centimetros: float) -> tuple[float, float]:
    """
    Converte metros e centímetros para pés e polegadas.
    1 metro = 3.28084 pés (ou 39.3701 polegadas)
    1 centímetro = 0.0328084 pés (ou 0.393701 polegadas)
    """
    pes_metros = metros * 3.28084
    pes_centimetros = centimetros * 0.0328084

    total_pes = pes_metros + pes_centimetros
    total_polegadas = (total_pes - int(total_pes)) * 12

    return int(total_pes), total_polegadas


def main():
    print("Calculadora de Metros e Centímetros para Pés e Polegadas")
    metros = float(input("Digite a quantidade de metros: "))
    centimetros = float(input("Digite a quantidade de centímetros: "))

    pes, polegadas = metros_e_cm_para_pes_e_polegadas(metros, centimetros)
    print(f"\nResultado: {pes} pés e {polegadas:.2f} polegadas")


if __name__ == "__main__":
    main()
    