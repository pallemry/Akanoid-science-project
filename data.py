import question
from typing import *

questions: Sequence[question.question_info] = [
    #1
    question.question_info(
        question="מהם החיידקים שגורמים לעששת?",
        answers=[
            "חיידקי S.mutans",
            "חיידקי M.sutans",
            "חיידקי S.sutans",
        ],
        correct_num=0,
        next=lambda x: print(x),
        fact="החיידקים שגורמים לעששת נקראים S.mutans"
    ),#2
    question.question_info(
        question="האם העששת גורמת רק לפגיעה במראה האסטטי?",
        answers=[
            "כן",
            "לא"
        ],
        correct_num=0,
        next=lambda x: print(x),
        fact="הידעתם? עששת עלולה להוביל לפגיעה רק במראה האסטתי"
    ),#3
    question.question_info(
        question="מה מקור השם עששת?",
        answers=[
            "עשש - חלב",
            "עשש - רעב",
            "עשש - אכילה",
            "עשש - חלש"
        ],
        correct_num=3,
        next=lambda x: print(x),
        fact="מקור השם עששת בא מהמילה עשש - חלש"
    ),#4
    question.question_info(
        question="עד כמה מחלת העששת מסוכנת?",
        answers=[
            "מאוד",
            "סכנת חיים",
            "לא מסוכנת",
            "עלולה לגרום לכאב"
        ],
        correct_num=2,
        next=lambda x: print(x),
        fact="מחלת העששת אינה מסוכנת"
    ),#5
    question.question_info(
        question="בכמה אחוזים מאוכלוסיות העולם היא פוגעת?",
        answers=[
            "5% - 20%",
            "21% - 30%",
            "31% - 40%",
            "41% - 60%",
            "420.69%"
        ],
        correct_num=2,
        next=lambda x: print(x),
        fact="30% - 40% מאוכלוסיות כדור הארץ סובלים מעששת"
    ),#6
    question.question_info(
        question="מה עלול לקרות כאשר ילדי \n צורכים תרופות על בסיס סירופ באופן קבוע?",
        answers=[
            "סוכרת סוג 1",
            "עששת",
            "סוכרת סוג 2",
            "דלקת",
            "שמנת"
        ],
        correct_num=1,
        next=lambda x: print(x),
        fact="ילדים שצורכים תרופות סירופ יקבלו עששת"
    ),#7
    question.question_info(
        question="האם עששת מדבקת?",
        answers=[
            "רק דרך קיום יחסי מין",
            "לא",
            "בדכ לא אבל מומלץ לשים מסיכה בקרב חולים",
            "כן"
        ],
        correct_num=1,
        next=lambda x: print(x),
        fact="העששת לא מדבקת"
    ),#8
    question.question_info(
        question="האם יש חיסון נגד עששת?",
        answers=[
            "כן",
            "לא",
            "החיסון הקיים מכיל שבבי מחשב של הממשלה"
        ],
        correct_num=1,
        next=lambda x: print(x),
        fact="אין חיסון נגד עששת"
    ),#9
    question.question_info(
        question="מהם הגורמים למחלה?",
        answers=[
            "גנטי + אכילה גרועה + היגיינה עוד יותר גרועה",
            "רק צחצוח שיניים",
            "שילוב של היגיינת הפה והפחתת סוכרים"
        ],
        correct_num=0,
        next=lambda x: print(x),
        fact="הגורמים למחלה הם: גנטיקה, היגיינה, תזונה"
    ),#10
    question.question_info(
        question="מתי התגלה קשר בין חיידקי הפה למחלה?",
        answers=[
            "1987",
            "1530",
            "2001",
            "1946",
            "1964"
        ],
        correct_num=3,
        next=lambda x: print(x),
        fact="הקשר בין חיידקי פה לעששת התגלה ב1946"
    )
]