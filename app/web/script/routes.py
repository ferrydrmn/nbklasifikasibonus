import os
import sys
import pickle
import numpy as np
from flask import render_template, url_for, request, redirect

from script import app
from script.forms import ClassificationForm

# Route Home
@app.route('/')
def home():
    form = ClassificationForm()
    return render_template('home.html', form=form)

# Route Klasifikasi
@app.route('/classification', methods=['GET', 'POST'])
def classification():
    if request.method == 'GET':
        redirect(url_for('home'))
    else:
        form = ClassificationForm()
        if form.validate_on_submit:
            
            # Mengambil data dari form
            card = int(form.card.data)
            call = int(form.call.data)
            block = int(form.block.data)

            # Memuat model yang telah dibuat
            sys.path.append(os.path.join(app.root_path, 'model'))
            filename = os.path.join(app.root_path, 'model/model.pkl')

            with open(filename, 'rb') as fs:
                clf = pickle.load(fs)
                result = clf.predict(np.array([card, call, block]))
                if result[0] == 0:
                    message = f'Pelanggan tersebut tidak layak menerima bonus!'
                else:
                    message = f'Pelanggan tersebut layak menerima bonus!'
                return render_template('home.html', form=form, message=message)

