// Functions for delivering primary reinforcement

class MonetaryReinforcer{
    constructor(bonus_usd_per_correct){
        this.bonus_total = 0
        this.bonus_per_correct = bonus_usd_per_correct || 0.0007 // one extra dollar for every 1000 correct 
    }

    async deliver_reinforcement(nreward){

        if(nreward >=1){
            this.bonus_total = this.bonus_total + this.bonus_per_correct
            console.log('Running monetary bonus amount',
              Math.round(this.bonus_total*1000)/1000)
          }
    }       
}



class JuiceReinforcer{
    constructor(juiceRewardPer1000){
      if (juiceRewardPer1000 != undefined){
        this.juiceRewardPer1000 = juiceRewardPer1000  
      }
      else{
        this.juiceRewardPer1000 = 300
      }
      
    }

    async deliver_reinforcement(nreward){

        if(nreward >=1){

            var RewardDuration = 0.5;

            if(port.connected == false){
              return
            }
            else if (port.connected == true){

                var p2 = port.writepumpdurationtoUSB(Math.round(RewardDuration*1000))
                return p2
            }
        }
      
        console.log('Delivered ', nreward, 'rewards')
    }

    setJuicerRewardDuration(){
      var m = 0;
      var b = 0;

      var pumpNumber = 1
      var liquidNumber = 2
      var rewardPer1000 = 300
      if (pumpNumber == 1){
        // m = 1.13; b = 15.04;
        m = 0.99; b = 14.78;
      } //peristaltic (adafruit)
      else if (pumpNumber == 2){
        // m = 3.20; b = -15.47;
        m = 1.40; b = -58.77;
      } //submersible (tcs)
      else if (pumpNumber == 3){
        // m = 0.80; b = -3.00;
        m=0.91; b = -15;
      } //diaphragm (tcs)
      else if (pumpNumber == 4){
        m = 0.0531; b=-1.2594;
      } //piezoelectric (takasago)
      else if (pumpNumber == 5){
        m = 2.4463; b=53.6418;
      } //new diaphragm (tcs)
      else if (pumpNumber == 6){
        if (liquidNumber==1 || liquidNumber==3){
          m=0.1251; b=-0.0833; //1=water 2=water-condensed milk 3=marshmallow slurry (4/30mL)
        }
        else if (liquidNumber==2){
          m=0.0550; b=0.6951; //water-condensed milk (50/50)
        }
      } //piezoelectric 7mL/min (takasago)
      return (rewardPer1000 - b)/m/1000;
      
    }
}