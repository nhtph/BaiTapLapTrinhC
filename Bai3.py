from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
    def string_to_int_list(self, string):
        return [int(num) for num in string.split()]

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr  # Trả về danh sách đã sắp xếp

    def button_sort_click(self, **event_args):
        try:
            numbers = self.text_box_input.text
            int_list = self.string_to_int_list(numbers)
            sorted_list = self.insertion_sort(int_list)  # Gọi hàm insertion_sort và lưu kết quả
            self.label_1.text = "Dãy số sau khi sắp xếp bằng Insertion Sort: " + ", ".join(map(str, sorted_list))
        except ValueError:
            alert("Vui lòng nhập các số nguyên cách nhau bằng dấu cách.")

if __name__ == '__main__':
    app = App(Form1)
    app.run() 