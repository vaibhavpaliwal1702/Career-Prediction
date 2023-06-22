from flask import *
import pickle
import numpy as np

md = pickle.load(open('careerPridiction.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


def bool(val):
    val = val.lower()
    if val == 'no':
        return "0"
    elif val == 'yes':
        return "1"
    else:
        pass


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        cgpa = request.form['cgpa']
        webd = request.form['webd']
        webd = bool(webd)
        da = request.form['da']
        da = bool(da)
        rws = request.form['rws']
        rws = bool(rws)
        tp = request.form['tp']
        tp = bool(tp)
        ntp = request.form['ntp']
        ntp = bool(ntp)
        c = request.form['c']
        c = bool(c)
        ad = request.form['ad']
        ad = bool(ad)
        cs = request.form['cs']
        cs = bool(cs)
        s = request.form['s']
        s = bool(s)
        db = request.form['db']
        db = bool(db)
        ds = request.form['ds']
        ds = bool(ds)
        eng = request.form['eng']
        eng = bool(eng)
        e = request.form['e']
        e = bool(e)
        tb = request.form['tb']
        tb = bool(tb)
        m = request.form['m']
        m = bool(m)
        ml = request.form['ml']
        ml = bool(ml)
        con = request.form['con']
        con = bool(con)
        lp = request.form['lp']
        lp = bool(lp)
        print(cgpa, webd, da, rws, tp, ntp, c, ad, cs, s, db, ds, eng, e, tb, m, ml, con, lp)
        input = np.array(
            [cgpa, webd, da, rws, tp, ntp, c, ad, cs, s, db, ds, eng, e, tb, m, ml, con, lp])
        print(input)
        print(type(input))
        res = (md.predict(input.reshape(-1, 19))[0])
        print(res)
        prof = ''
        if (res == 0):
            prof = 'Analyst'
        elif (res == 1):
            prof = 'Content Writer'
        elif (res == 2):
            prof = 'Data Analysis'
        elif (res == 3):
            prof = 'Data Engineer'
        elif (res == 4):
            prof = 'Developer'
        elif (res == 5):
            prof = 'ML Engineer'
        elif (res == 6):
            prof = 'Management'
        elif (res == 7):
            prof = 'Marketing'
        elif (res == 8):
            prof = 'Network Engineer'
        elif (res == 9):
            prof = 'Security'
        return render_template('result.html', res=prof)


if __name__ == '__main__':
    app.run(debug=True)
