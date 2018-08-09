from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


texts = ['<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. <mark>Et non ex maxima parte de tota iudicabis?</mark> Si stante, hoc natura videlicet vult, salvam esse se, quod concedimus; Sedulo, inquam, faciam. Qui non moveatur et offensione turpitudinis et comprobatione honestatis? Et non ex maxima parte de tota iudicabis? <b>Duo Reges: constructio interrete.</b> Beatus autem esse in maximarum rerum timore nemo potest. <b>Quis istud possit, inquit, negare?</b></p>',
         '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cave putes quicquam esse verius. <b>Sed ego in hoc resisto;</b> <mark>Dic in quovis conventu te omnia facere, ne doleas.</mark> Duo Reges: constructio interrete. <i>Zenonis est, inquam, hoc Stoici.</i> Hanc ergo intuens debet institutum illud quasi signum absolvere. Nam illud vehementer repugnat, eundem beatum esse et multis malis oppressum. Nam si amitti vita beata potest, beata esse non potest. Sed ad bona praeterita redeamus. Animum autem reliquis rebus ita perfecit, ut corpus; Nos paucis ad haec additis finem faciamus aliquando; Equidem soleo etiam quod uno Graeci, si aliter non possum, idem pluribus verbis exponere.</p>',
         '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nescio quo modo praetervolavit oratio. Duo Reges: constructio interrete. Sed ne, dum huic obsequor, vobis molestus sim.</p>']


@app.route('/first')
def first():
    return texts[0]


@app.route('/second')
def second():
    return texts[1]


@app.route('/third')
def third():
    return texts[2]
