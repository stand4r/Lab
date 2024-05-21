def extract_class_fields(class_text):
    # Разделяем текст на строки
    lines = class_text.split('\n')
    
    # Инициализируем список для хранения описаний полей
    field_descriptions = []
    
    # Проходим по каждой строке
    for line in lines:
        # Убираем лишние пробелы
        line = line.strip()
        
        # Проверяем, является ли строка описанием поля
        if (line.startswith("public") or line.startswith("private") or line.startswith("protected")) and "class" not in line and "()" not in line:
            # Добавляем строку в список описаний полей
            field_descriptions.append(line)
    
    return field_descriptions

# Пример использования
class_text = """
public class SampleClass {
    public int field1;
    private string field2;
    protected bool field3;
    public void Method1() { }
    private int Method2() { }
}
"""

field_descriptions = extract_class_fields(class_text)
for field in field_descriptions:
    print(field)
