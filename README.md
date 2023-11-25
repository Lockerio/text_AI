# TextAI

___

### This project was created for an internship at "LEMZ-T".
It was necessary to write a neural network that is able to recognize numbers and letters.

Аnd more specifically: I was needed to write system to recognize russian car numbers.

---

### How does it work?
This is a web-site, where you can draw or upload symbols to get them in text form.

1) If you choose to draw or upload only one file, the digits neural network will be used;

2) If you choose to upload 8 symbols (like in russian car numbers), you will have to upload 
files with correct sequence of symbols, because 2, 3, 4, 7, 8 are digits (digits neural
network will be used) and others are letters (letters neural
network will be used). \
So, if you fail the sequence, you will get wrong results.

PS: There are 3 networks in project. So, "ru_car_numbers_recognition_by_symbol" is a
failed experiment, so ignore it. 

---

### Technology stack

1) **TensorFlow** and **Keras** - creating neural networks;
2) **PIL** - working with images;
3) **Flask** - creating backend for a web-site;
4) **HTML / CSS** - creating frontend for a web-site;
5) **JS** - creating a drawing element in the web-site. 