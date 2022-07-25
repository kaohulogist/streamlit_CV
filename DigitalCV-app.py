import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
#from streamlit_lottie import st_lottie_spinner

# https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Digital CV", page_icon=":coffee:")

def load_lottie_url(url):
  r = requests.get(url)
  if r.status_code !=200:
    return None
  return r.json()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# ---- LOAD ASSETS ----
lottie_coding = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_ndj9fzcd.json")


with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

############
# Header
st.write('''
# Khoa V.D Huynh, BSEE
##### *Resume*
''')

image = Image.open('KH.png')
st.image(image, width=200)

st.markdown('## Sumary', unsafe_allow_html=True)

with st.container():
  left, right = st.columns([4,1])
  with left:    
    st.info('''
    Dedicated Electrical Engineer recent graduate with project experience in design and development of the system.
    A fast and attentive learner candidate who enjoys being part of a team to support the development of engineering projects.
    ''')
  with right:
    st_lottie(lottie_coding, height=150, key="spaceman")

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: Gray;">
  <a class="navbar-brand" href="/" target="_blank">Khoa V.D Huynh</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#project">Project</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#ee">IIot | PLC | HMI | SCADA</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt2_51(a,b):
    col1, col2 = st.columns([5,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2_41(a,b):
    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2_14(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt2_12(a,b):
    col1, col2 = st.columns([2,3])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt4_1311(a,b,c,d):
  left, mid1, mid2, right = st.columns([1,3,1,1])
  with left:
    st.markdown(a)
  with mid1:
    st.markdown(b)
  with mid2:
    st.markdown(c)
  with right:
    st.markdown(d)
  

#####################
st.markdown('''
## Education
''')
txt2_51('**Bachelors of Science** (Electrical Engineering), *University of Texas at Tyler*', '2020-2022')
st.markdown(''' 
- Graduated with Latin Honors.
- Member of IEEE & Phi Sigma Pi National Honor Fraternity.
''')
txt2_51('**Associate of Science** (Computer Science), *Houston Community College*, Texas',
'2018-2020')
st.markdown('''
- Received Leadership Excellent Scholarship.
- Achieved scholastic distinction for President's List, Dean's List, and Honor Roll.
''')


#####################
st.markdown('''
## Work Experience
''')

txt2_41('**Vinny AC, Houston, TX** *(AC Technician Associate)*','06/2021 - present')
st.markdown('''
- Diagnosed and repaired electrical and mechanical faults to home HVAC systems.
- Operated equipment installations with safe work habits when working in a team environment.
- Tested the systematic product to follow standard NEC concepts, practices, and procedures.
- Provided excellent communication guidance to clients on maintaining applications, increasing contracts by 20%.
''')

txt2_41('**NASA Texas Space Grant Consortium Design Challenge, Houston, TX**','09/2021 - 06/2022')
txt2_41('**Vehicle Interchangeable Electronic Controller (VIEC) Network System**','')
txt2_41('*(HEC5 Team – Technical Design System Lead)*','')
st.markdown('''
-	Designed and implemented a system of interchangeable controllers to interact with multiple sensors (analog & digital) for automation performing the appropriate program accordingly to a positional identifier.
-	Extracted data to store in a database. Displayed share data virtually via a GUI application by Python programming.
-	Collaborated with team members to assign suitable role skills, resulting in timely completion within budgetary $1000 limitations. Monitored and controlled the project via Git.
-	Tested components, sub-systems, codes, and wiring connections to determine the failures.
-	Generated AutoCAD 3D modeling and applied 3D printing to complete prototype.
-	Achieved a highly reliable product with better than 90% success for each interchangeable swapping run.
-	Experienced with electrical testing equipment voltmeters, oscilloscopes, power supply, soldering, and silicone seal for technical troubleshooting and designing an electric control system.
-	Won top 7 NASA TSGC design award.
''')

txt2_41('**U.S. Department of Commerce, Katy, TX** *(IT Support)*','05/2020 - 11/2020')
st.markdown('''
-	Provided technical assistance to users via Citrix Workspace, Remedy, and Information Admission tools.
-	Coordinated with each manager of a group of 25 persons to install remote updates to prevent service disruption and resolve technical issues.
-	Applied information security to monitor account credentials.
-	Performed work with a proficiency level in MS Office, Outlook, PowerPoint, OneNote, Word, Excel, and Outlook. 
''')

txt2_41('**US Jaclean, Stafford, TX** *(Manager)*','05/2016 – 09/2019')
st.markdown('''
-	Managed the Houston brand office to generate revenue from vending, retail, wholesale, and delivery.
-	Organized teams to meet deadlines, and distribute products from warehouse to stores. Validated non-working massage chair units for replacements or repairs for hardware and software. 
-	Documented resources management to maintain operation and control.
''')

txt2_41('**9c Studio, Richmond, TX** *(Cinematography Freelance)*','2017 - present')
st.markdown('''
- Building a freelance business on customized fine art storytelling wedding videos from cinematic visual elements: lighting, camera setup, color, edit.
''')


#####################
st.markdown('''
## Project:
''')
txt4_1311('*S&P 500 Stock Price*',
 'A data-driven web application in Python for webscraping S&P500 stock prices and plotting the Closing Price year-to-date. Featuring customzied function on single input ticker plotting and listing tickers from favorite sectors.',
  '[GitHub repo](https://github.com/kaohulogist/sp500-WebApp)'
  , '[`WEB DEMO`](https://kaohulogist-sp500-webapp-sp500-app-ks8y61.streamlitapp.com/)')



#####################
st.markdown('''
## Skills:
''')
txt2_12('Programming', '`Python` `Go` `C++` `Matlab` `LabVIEW`')
txt2_12('System Integration | Embedded', '`PLC` `SCADA` `IIot`')
txt2_12('Data Processing | Visualization', '`SQL` `pandas` `numpy` `matplotlib` `seaborn`')
#txt2_12('Penetration Testing | Cyber Security', '`Kali Linux`, `CompTIA Security+`')
txt2_12('Machine Learning | Deep Learning' , '`scikit-learn` `keras` `TensorFlow`')
txt2_12('Web Development | Deployment', '`HTML` `CSS` `Markdown` `streamlit` `Heroku`')



#####################
st.markdown('''
## Social Media
''')
txt2_14('LinkedIn', 'www.linkedin.com/in/khoa-vd-huynh')
txt2_14('GitHub', 'https://github.com/kaohulogist')
txt2_14('Online CV', 'https://kaohulogist-streamlit-cv-digitalcv-app-mr0gi1.streamlitapp.com/')