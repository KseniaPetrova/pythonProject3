# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

vklad_T = 100000
mecyac = 7
#Tincoff
procent_T = 0.17
procentOfRub_T = vklad_T * procent_T / 12
print('Получуза месяц в тинькофф', procentOfRub_T)

for i in range(1, mecyac + 1):
    procent_of_rub = vklad_T * procent_T / 12
    vklad_T += procent_of_rub
print(vklad_T)

vklad_S = 100000
#Sber
procent_S = 0.18
poluchu_S = vklad_S * 0.18 / 12 * mecyac
print(poluchu_S + vklad_S)  # 10500
print(poluchu_S + vklad_S - vklad_T)
procentOfRub_S = vklad_S * 0.18 / 12
print('Получуза месяц в тинькофф', procentOfRub_S)
print(procentOfRub_S - procentOfRub_T)