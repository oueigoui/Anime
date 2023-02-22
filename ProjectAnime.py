import joblib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import streamlit as st



def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20210222/pngtree-white-line-background-business-image_564059.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()

st.title('Number of :red[Viewers]')
left, right = st.columns(2)
left.markdown("Views per story?")
left.markdown("by the user filling in the title")


data = pd.read_csv('Ani.csv')
search_term = st.text_input("Name Anime 📌")
if search_term:
    filterd_data = data[data["Anime"].str.contains(search_term, case=False)]
    st.dataframe(filterd_data)

else:
    if st.image:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image('https://cms.dmpcdn.com/movie/2020/07/31/5a050d20-d2dc-11ea-95c1-937722e3d7f7_original.png', width=300)
            st.write('One Piece ☠')
        with col2:
            st.image('https://wannasin.s3.ap-southeast-1.amazonaws.com/news/attach/FtGG3HfbrCbB2THC.jpg', width=300)
            st.write('Blue Lock ⚽️')
        with col3:
            st.image('https://images-na.ssl-images-amazon.com/images/S/pv-target-images/071eaab97e0330777dac3809a91eafa06d410b1c61baefc06d51288bbbdbaede._RI_V_TTW_.jpg', width=225)
            st.write('Conan 🦾')


def load_Ani_data():
    return pd.read_excel('Ame.xlsx')


def save_model(model):
    joblib.dump(model, 'model.joblib')


def load_model():
    return joblib.load('model.joblib')

generateb = right.button('generate Ame.xlsx')


def generate_Ame_data():
    pass

if generateb:
    right.write('generating "Ame.xlsx" ...')
    generate_Ame_data()
    right.write(' ... done')

loadb = right.button('load Ame.xlsx')
if loadb:
    right.write('loading "Ame.xlsx ..."')
    df = pd.read_excel('Ame.xlsx', index_col=0)
    right.write('... done')
    right.dataframe(df)
    fig, ax = plt.subplots()

trainb = right.button('trainb คนดูต่อเรื่อง')
if trainb:
    right.write('training model ...')
    df = pd.read_excel('Ame.xlsx', index_col=0)
    model = LinearRegression()
    right.write('... done')
    right.dataframe(df)
    save_model(model)

Anime = st.sidebar.button("Anime 🕵️‍♀")
if Anime:
    st.title('Im going to :green[introduce the Anime🙏]')
tab1, tab2, tab3, tab4 = st.tabs(["Together⚓⚽🖥 ", "One Piece ⚓", "Blue Lock ⚽", "Conan 🖥"])

with tab1:
    st.write("ANIME :red[HITS 😱😱😱]")
    st.image('https://sgp1.vultrobjects.com/img-in-th/UKTaOp.jpeg',width=700)
    st.markdown("<h1 style='text-align: center; color: red;'>Welcome Anime 😜 </h1>", unsafe_allow_html=True)

with tab2:
    st.header("Anime :red[One] Piece ⚓⛵")
    st.image('https://cheezelooker.com/file_managers/uploads/file_managers/source/2020%20DAILY%20CULTURE/APRIL/WEEK%204/'
             'ONE%20PIECE%20NETFLIX%20RELEASE%20DATE%20REVEALED/https___hypebeast.com_image_2020_01_netflix-orders-one-piece-'
             'live-action-series-tomorrow-studios-info-001.jpg',width=700)
    st.write('')
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Story 👉'):
            st.write(
                'One Piece เล่าเรื่องราวของหนุ่มน้อย ลูฟี่ ที่ปรารถนาจะค้นพบมหาสมบัติวันพีซและได้รับการขนานนามว่าเป็นเจ้าแห่งโจรสลัดในโลกสมมติที่มีพื้นผิวเป็นทะเลเกือบทั้งหมดฟี่ต้อง'
                'ออกเรือไปยังทะเลกว้างใหญ่ไพศาลเข้าไปยัง‘แกรนด์ไลน์’ ทะเลที่ใหญ่ที่สุดในโลกซึ่งตั้งอยู่ตรงเส้นศูนย์สูตร แล้วออกเดินเรือผจญภัยไปรอบโลกเพื่อที่จะไปถึงเกาะสุดท้าย รัฟเทล '
                'ที่ว่ากันว่าสมบัติวันพีซถูกเก็บไว้ที่นั่นวันที่ 22 กรกฎาคม 1997 จุดเริ่มต้นที่ความฝัน:ประเด็นหลักที่ใหญ่ที่สุดของเรื่อง One Piece  คือความฝันลูกเรือทุกคนบนเรือเธาซันด์ ซันนี'
                ' ล้วนมีความฝันสูงสุดที่ต้องทำให้สำเร็จไม่ว่าจะเป็นลูฟี่ที่ต้องการเป็นเจ้าแห่งโจรสลัดนักดาบโซโลที่อยากเป็นนักดาบที่เก่งที่สุดในโลกต้นหนเรือนามิที่อยากเขียนแผนที่โลกให้สำเร็จไปจน'
                'ถึงนิโคโรบินลูกเรือนักประวัติศาสตร์ที่อยากค้นหาประวัติศาสตร์100ปีที่หายไปของโลกใบนี้ความฝันเป็นประเด็นที่เข้าถึงง่ายแต่ทรงพลังการสร้างเจตจำนงให้ตัวละครอย่างเด่นชัดเป็นการสร้าง'
                'พลังให้กับคนอ่านไปด้วยในตัวอีกทั้งอุปนิสัยของตัวละครเอกอย่างลูฟี่ยังเป็นคนที่มุ่งมั่นเชื่อมั่นในตัวเองพัฒนาตัวเองไม่หยุดยั้งและรักในพวกพ้องซึ่งแน่นอนว่าคนอ่านเกือบทุกคนย่อมอยากเป็น'
                'คนแบบนี้อิสระเสรีที่ไม่ถูกปิดกั้น:')
        else:
            st.write('')
            with col2:
                if st.button('Album 📸 '):
                    st.image('https://thestandard.co/wp-content/uploads/2018/07/CULTURE-%E0%B8%84%E0%B8%A3%E0%B8%9A%E0%B8%A3%E0%B8%AD%E0%B8%9A'
                             '-21-%E0%B8%9B%E0%B8%B5-One-Piece-%E0%B8%A1%E0%B8%AB%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%9E%E0%B8%A2%E0%B9%8C%E0%B8%81%'
                             'E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%95%E0%B8%B9%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%'
                             'E0%B8%A1%E0%B8%B2%E0%B8%81%E0%B8%81%E0%B8%A7%E0%B9%88%E0%B8%B2%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%'
                             'E0%B8%82%E0%B8%AD%E0%B8%87%E0%B9%80%E0%B8%94%E0%B9%87%E0%B8%81_cover_.jpg',width=500)
                    st.write('Figure 1')
                    st.image('https://thethaiger.com/th/wp-content/uploads/2022/03/Wano_Country_Arc.jpg',width=500)
                    st.write('Figure 2')
                    st.image('https://thestandard.co/wp-content/uploads/2021/10/One-Piece.jpg',width=500)
                    st.write('Figure 3')
                    st.image('https://i0.wp.com/inzpy.com/wp-content/uploads/2022/06/1-7.jpg?resize=696%2C446&ssl=1',width=500)
                    st.write('Figure 4')
                    st.image('https://sites.google.com/site/projectonepiece1/_/rsrc/1492653441915/prawati/cropped-cool-backrounds-one-piece-31311311'
                             '-600-3751.png?',width=500)
                    st.write('Figure 5')

with tab3:
    st.header("Anime Blue :blue[Lock⚽️🥇]")
    st.image('https://thethaiger.com/th/wp-content/uploads/2022/11/Blue-Lock-%E0%B8%A1%E0%B8%B1%E0%B8%87%E0%B8%87%E0%B8%B0.jpg',width=700)
    st.write('')
    col3, col4 = st.columns(2)
    with col3:
        if st.button('story👉'):
            st.write(
                'Blue Lock เป็นอนิเมะกีฬาที่สุดจริง ๆ ครับ ทั้งความแปลกใหม่และความเดือดของเนื้อเรื่อง เริ่มจากอนิเมะกีฬาทั่วไปจะมีการพูดถึงมิตรภาพ ความสามัคคีซะเยอะอาจจะมีช่วงที่มีความขัดแย้งเกิดขึ้น'
                'บ้างแต่ก็เล็กน้อยบรรยากาศโดยรวมแล้วจะสบาย ๆ แต่ไม่ใช่กับ Blue Lock ที่เปิดมาด้วยความสิ้นหวังและพ่ายแพ้ของตัวละครเอกตามมาพร้อมๆกับการเอาชีวิตรอดใน Blue Lock ที่มีคู่แข่งถึง 299 คน'
                ' ถึงฟุตบอลจะต้องเล่นกันเป็นทีมแต่ลึกๆแล้วเราคนดูก็รู้ว่าพวกชนะมีได้แค่คนเดียวเท่านั้นเรื่องนี้ได้ถูกพูดถึงซ้ำๆจากตัวละครคนอื่นในเรื่องสร้างความรู้สึกว่าต้องเอาตัวรอดต้องชนะเท่านั้นพูดง่ายๆว่าผสมความเป็น '
                'battle royaleเข้าไปซึ่งถือว่าแปลกใหม่มากสำหรับอนิเมะแนวกีฬาตามตลาดทั่วไปครับและเป็นเรื่องราวของชายหนุ่มโยอิจิ อิซางิ ชายหนุ่มที่ชื่นชอบกีฬามาตั้งแต่ยังเด็ก เขาได้แพ้ในการแข่งขันทีมฟุตบอล'
                'ของมัระดับมัธยมด้วยการตัดสินใจเพียงแค่เพียงเสี่ยววินาที เขารู้ผิดหวังและสึกสับสนในตัวเองที่ฝันว่าจะเป็นแนวหน้าอันดับหนึ่ง แต่ระหว่างนั้นเขาได้รับจดหมายจากสมาคมฟุตบอลญี่ปุ่นที่คิดจะปฏิวัติการแข่งฟุตบอล'
                'ขึ้นมาใหม่โดยเชิญให้เข้าร่วมโครงการ Blue Lockที่รวมนักเตะแนวหน้าระดับเอส มาแข่งขันกันเพื่อเป็นแนวหน้าอันดับหนึ่งของโลก')
        else:
            st.write('')
            with col4:
                if st.button('album 📸 '):
                    st.image('https://imgmedia.larepublica.pe/1200x660/lol/original/2022/10/08/6341aa327b2c7018db6c8102.jpg', width=500)
                    st.write('Figure 1')
                    st.image('https://areajugones.sport.es/wp-content/uploads/2022/08/blue-lock-anime-fecha.jpg', width=500)
                    st.write('Figure 2')
                    st.image('https://www.booska-p.com/wp-content/uploads/2022/12/Blue-Lock-Thailande-Visu-News.jpg', width=500)
                    st.write('Figure 3')
                    st.image('https://pbs.twimg.com/media/EkiVX1AUYAAreS0.jpg', width=500)
                    st.write('Figure 4')
                    st.image('https://media.techtribune.net/uploads/2022/12/blue-lock-3.jpg', width=500)
                    st.write('Figure 5')
                else:
                    st.write('')

with tab4:
    st.header("Anime Co:red[nan💻]")
    st.image('http://cartoon.mthai.com/app/uploads/2011/04/1272117227.jpg', width=700)
    st.write('')
    col5, col6 = st.columns(2)
    with col5:
        if st.button('STORY 👉'):
            st.write(
                'คุโด้ ชินอิจิ ยอดนักสืบนักเรียนมัธยมปลาย วัย 17 ปี ถูกขนานนามว่า "ยอดนักสืบแห่งยุคเฮเซย์" วันหนึ่งไปเที่ยวกับเพื่อนสมัยเด็กที่ชื่อโมริ รัน หลังจากเป็นแชมป์คาราเต้ระดับเขตหลังปิดคดีได้'
                'ชินอิจิแอบไปรู้เห็นเจรจาลับของชายชุดดำโดยไม่ระวังถูกชายชุดดำอีกคนทำร้ายก่อนสลบถูกจับกรอกยาพิษAPTX4869 ที่องค์กรคิดค้นขึ้นแต่ยาพิษนั้นกลับทำให้ชินอิจิตัวเล็กลงจนกลายเป็นเด็กอายุ 7 '
                'ขวบและเปลี่ยนชื่อใหม่เป็นเอโดงาวะ โคนัน ด้วยความช่วยเหลือของ ดร.อากาสะ ฮิโรชิ เพื่อสืบหาเบาะแสร่องรอยของชายชุดดำและเพื่อนำยาพิษมาหาทางรักษาให้คืนร่างได้ไปอยู่กับโมริ รัน '
                'ที่สำนักงานนักสืบโมริ ซึ่งคุณพ่อของรัน โมริ โคโกโร่เป็นนักสืบเอกชนแต่ก็พึ่งไม่ได้โคนันจึงได้ใช้สติปัญญาของตนกับสิ่งประดิษฐ์ของ ดร.อากาสะ ฮิโรชิ คลี่คลายคดีต่างๆแทนเพื่อให้โคโกโร่มีชื่อเสียง'
                'ขึ้นมาและรอผู้จ้างวานที่จะได้เบาะแสของชายชุดดำเพราะอยู่ในร่างของเด็กจึงต้องกลับไปเรียนชั้น ป.1 ที่โรงเรียนประถมเทตันใหม่อีกครั้งและได้ก่อตั้งขบวนการนักสืบเยาวชนกับเพื่อนร่วมชั้นอย่าง โยชิดะ อายูมิ,'
                ' ซึบุรายะ มิซึฮิโกะ, และ โคจิมะ เก็นตะ การสืบหาชายชุดดำและยาแก้พิษของโคนันก็ได้เรื่อยมาได้เกิดคดีต่างๆและค้นพบบุคคลสำคัญต่างๆที่เกี่ยวข้องกับพวกชายชุดดำมากขึ้นอย่าง มิยาโนะ อาเคมิ 1 '
                'ในสมาชิกปลายแถวในองค์กรชุดดำ มิยาโนะ ชิโฮะ หรือ ไฮบาระ ไอ มีโค้ดเนมว่าเชอร์รี่อดีตสมาชิกองค์กรชุดดำและนักวิทยาศาสตร์ 1 ในทีมคิดค้นยา APTX4869 ที่ทำให้โคนันตัวเล็กลง มาช่วยหาทางทำ'
                'ยาคืนร่าง แต่มีผลแค่ชั่วคราวตลอด หลังมีข่าว คุโด้ ชินอิจิมีชีวิตอยู่ หลังหายสาปสูญไปนาน แพร่ไปทั่ว(โคนันกินยาคืนร่างชั่วคราวไปทัศนศึกษากับโรงเรียน แต่พัวพันกับคดี)โชคดีที่พวกคนที่รู้ตัวจริงของโคนัน'
                'ช่วยปิดข่าวทันครอบครัวคุโด้จึงรวมตัวปรึกษากันเรื่องเบาะแสของคนที่ถูก RUM ฆ่าก่อนตายทิ้งไว้กับโค้ดของ RUM มาสลับกันจนรู้ว่าบอสเกี่ยวข้องกับคาราสุมะ เรนยะ(เศรษฐีที่มีอำนาจทางการเมืองที่สุดในญี่ปุ่นที่'
                'น่าจะตายไปแล้วในอดีต) พ่อแม่จึงคิดอยู่ญี่ปุ่นเพื่อคิดแผนหาทางช่วย ซึ่งคือการยืนยันว่าถึงครึ่งเรื่องแล้ว')
        else:
            st.write('')
    with col6:
        if st.button('ALBUM 📸 '):
            st.image('https://lifestyle.campus-star.com/app/uploads/2017/11/conan-cover.jpg', width=500)
            st.write('Figure 1')
            st.image('https://travel.marumura.com/wp-content/uploads/2021/12/Detective-Conan-World-Universal-Cool-Japan-2022.jpg', width=500)
            st.write('Figure 2')
            st.image('https://inwfile.com/s-df/mquqfh.jpg', width=500)
            st.write('Figure 3')
            st.image('http://cartoon.mthai.com/app/uploads/2011/04/detective-conan-wallpaper.jpg', width=500)
            st.write('Figure 4')
            st.image('https://www.kartoon-discovery.com/focus/images/mpic_conan.jpg', width=500)
            st.write('Figure 5')
        else:
            st.write('')
