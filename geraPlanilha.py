import openpyxl
import pandas as pd

def process_file(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active

    data = []
    item = {}
    title_counts = {}

    for row in sheet.iter_rows(values_only=True):
        if not any(row):  # Verifica se a linha está vazia
            if item:
                data.append(item)
                item = {}
                title_counts = {}
            continue

        current_title = None
        for i in range(0, len(row)):
            cell = row[i]
            if isinstance(cell, str) and ":" in cell:
                current_title = cell.split(':')[0].strip()
                title_counts[current_title] = title_counts.get(current_title, 0) + 1
                if title_counts[current_title] > 1:
                    current_title = f"{current_title}{title_counts[current_title]}"
                value_index = i + 1
                while value_index < len(row) and (not row[value_index] or ":" in str(row[value_index])):
                    value_index += 1
                value = row[value_index] if value_index < len(row) else None

                if current_title == "Resumo":
                    # Se o título for "Resumo" e a célula à direita contiver dados, adiciona a célula à direita como valor/descrição do resumo
                    description = str(row[i + 1]) if i + 1 < len(row) and row[i + 1] else ""
                    item[current_title] = description
                elif value is not None:
                    item[current_title] = value

                current_title = None

    if item:
        data.append(item)

    df = pd.DataFrame(data)
    return df

df = process_file('Portugal - Manuscritos.xlsx')
df.to_excel('saida.xlsx', index=False)
