{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "83a01c79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import joblib\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "model = joblib.load(\"model.pkl\")\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "\n",
    "    features = [float(x) for x in request.form.values()]\n",
    "    \n",
    "    prediction = model.predict([features])\n",
    "\n",
    "    return render_template(\n",
    "        'index.html',\n",
    "        prediction_text=f'Prediction: {prediction[0]}'\n",
    "    )\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True, use_reloader=False)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv (3.14.4)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
