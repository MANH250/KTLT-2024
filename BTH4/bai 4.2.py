def remove_invisible_chars(text):
    # Loại bỏ dấu cách và dấu tab
    return text.replace(" ", "").replace("\t", "")

# Ví dụ ban đầu
example_text = "Đây là một ví dụ với dấu cách và \t dấu tab."

# Sử dụng hàm để loại bỏ các ký tự không nhìn thấy
cleaned_text = remove_invisible_chars(example_text)

print("Chuỗi sau khi loại bỏ các ký tự không nhìn thấy:")
print(cleaned_text)
