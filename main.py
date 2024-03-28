from flask import Flask,render_template,request
import pred as m
import os
app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        milestones=request.form["milestones"]
        is_top500=request.form["is_top500"]
        has_roundB=request.form["has_roundB"]
        funding_rounds=request.form["funding_rounds"]
        age_last_milestone_year=request.form["age_last_milestone_year"]
        avg_participants=request.form["avg_participants"]
        has_roundA=request.form["has_roundA"]
        has_roundC=request.form["has_roundC"]
        has_roundD=request.form["has_roundD"]
        age_first_milestone_year=request.form["age_first_milestone_year"]
        is_enterprise=request.form["is_enterprise"]
        age_last_funding_year=request.form["age_last_funding_year"]
        is_advertising=request.form["is_advertising"]
        funding_total_usd=request.form["funding_total_usd"]
        is_software=request.form["is_software"]
        is_mobile=request.form["is_mobile"]
        is_consulting=request.form["is_consulting"]
        is_biotech=request.form["is_biotech"]
        is_web=request.form["is_web"]
        is_gamesvideo=request.form["is_gamesvideo"]
        is_othercategory=request.form["is_othercategory"]
        is_TX=request.form["is_TX"]
        has_VC=request.form["has_VC"]
        is_ecommerce=request.form["is_ecommerce"]
        has_angel=request.form["has_angel"]
        age_first_funding_year=request.form["age_first_funding_year"]

        status_pred = m.prediction(milestones, is_top500, has_roundB, funding_rounds, age_last_milestone_year,
               avg_participants, has_roundA, has_roundC, has_roundD, age_first_milestone_year, 
                is_enterprise, age_last_funding_year, is_advertising, 
               funding_total_usd, is_software, is_mobile, is_consulting, is_biotech, is_web,
               is_gamesvideo, is_othercategory, is_TX, has_VC, is_ecommerce, has_angel, 
               age_first_funding_year)

        outcome=""
        print(status_pred)
        temp=status_pred[1]

        if(temp[0]==1):
            outcome="You're doing great! Keep up the good work."
        elif(temp[0]==0):
            outcome="According to statistics, your startup needs work to achieve more milestones."
        else:
            outcome=f"{temp}"
    return render_template("sub.html",n=outcome,match_1=status_pred[0],match_2=status_pred[2],match_3=status_pred[3])
if __name__=="__main__":
#     app.run()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
