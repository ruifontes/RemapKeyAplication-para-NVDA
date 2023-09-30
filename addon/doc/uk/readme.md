# Remap Applications key


## Інформація
* Автори: Rui Fontes, засновано на роботі від Héctor J. Benítez Corredera
* Оновлено 30/09/2023
* Завантажити [стабільну версію][1]
* Сумісність: NVDA версія 2019.3 і пізніші


## Опис
Простий додаток для тих комп’ютерів, які не мають клавіші контекст або клавіша контекст у яких не працює.
Вам потрібно буде призначити клавішу або комбінацію клавіш, які виконуватимуть функцію клавіші контекст.
Потрібну комбінацію можна призначити в меню NVDA / Параметри / Жести вводу... / RemapKeyAplication.


## Огляд
Призначаючи комбінацію клавіш або одну клавішу, ви повинні переконатися, що ця комбінація або клавіша не використовується в жодному додатку.
Наприклад, Ctrl + стрілка вниз може працювати для більшої частини системи, але в Google Chrome видасть помилку, не дозволяючи отримати доступ до контекстного меню.
Для прикладу, я зазвичай використовую клавішу «Друк екрана» (printScreen), яка зазвичай знаходиться у верхньому рядку праворуч і зазвичай є другою або третьою клавішею.
Ви можете дізнатися, яка це клавіша, якщо скористаєтесь довідкою введення NVDA; для цього натисніть клавішу NVDA + 1 і починайте вивчати клавіші на клавіатурі. Коли почуєте «Друк екрана», це і буде та клавіша, яку ви шукали. Ми можемо вийти з підказки введення NVDA, натиснувши NVDA + 1 ще раз.
Це лише приклад, і користувач може сам вибрати потрібну клавішу або комбінацію клавіш.


## Перекладачі й учасники:
* Іспанська: Rémy Ruiz
* Французька: Rémy Ruiz
* Російська: Valentin Kupriyanov
* Українська: VovaMobile
* Турецька: Umut Korkmaz


## Журнал змін


### Версія 2023.09.02
* Наразі додаток підтримують Rui Fontes та португальська команда NVDA
* Тепер код базується на англійській мові.


### Версія 0.4
* Додано російську, українську й турецьку мови.
* Додано сумісність із NVDA 2023.1


### Версія 0.3
* Changed the way to invoke the applications key from native NVDA to native Windows, since it is a more reliable and more direct method.
* Added the possibility of left and right mouse clicks on focus.
We will have to assign the corresponding key combinations in the Input gesture dialog.
When we execute the action, the mouse will move to the focus and make the corresponding click, and a sound will be heard indicating that the click was executed.


### Version 0.2
* Compatibility with NVDA 2022


### Version 0.1.5
* Fixed issue in NVDA add-ons.
* Added French language.


### Version 0.1
* Initial version.

[1]: https://github.com/ruifontes/RemapKeyAplication-para-NVDA/releases/download/2023.09.30/remapApplicationsKey-2023.09.30.nvda-addon
