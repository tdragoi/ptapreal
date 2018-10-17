import construct_landing_page as c 
reload(c)

SAVE_LOCATION = '../public/landing_pages/examples/'
def makeInLabMTS(): 
    IMAGEBAGS = 'https://s3.amazonaws.com/milresources/ImageBagMetaDefinitions/MutatorTraining_FullVarWithBGSetA.json'

    GAME = {'gameId':'example_inlab_MTS',
          "periodicRewardIntervalMsec":60000,
          "periodicRewardAmount":1,
          "onFinish":"continue",
          "randomSeed":'none',
    }

    TASK_SEQUENCE = [{
                  "taskType":"MTS", 
                  "sampleBagNames":['FullVarWithBGSetA_batch0obj0', 'FullVarWithBGSetA_batch0obj1', 
                  'FullVarWithBGSetA_batch0obj2'], 
                  "fixationXCentroid":0.5,
                  "fixationYCentroid":0.8,
                  "fixationDiameterDegrees":3,
                  "sampleXCentroid":0.5,
                  "sampleYCentroid":0.5,
                  "sampleDiameterDegrees":8,
                  "actionXCentroid":[0.3, 0.7], 
                  "actionYCentroid":[0.8, 0.8],
                  "actionDiameterDegrees":[6, 6],
                  "choiceXCentroid":[0.3, 0.7],
                  "choiceYCentroid":[0.8, 0.8],
                  "choiceDiameterDegrees":[4, 4],
                  "choiceMap":{"FullVarWithBGSetA_batch0obj0":"FullVarWithBGSetA_batch0obj0", 
                  "FullVarWithBGSetA_batch0obj1":"FullVarWithBGSetA_batch0obj1", 
                  'FullVarWithBGSetA_batch0obj2':"FullVarWithBGSetA_batch0obj2"}, 
                  "sampleOnMsec":200, 
                  "sampleOffMsec":0,
                  "choiceTimeLimitMsec":5000,
                  "punishTimeOutMsec":100,
                  "punishStreakTimeOutMultiplier":1,
                  "rewardTimeOutMsec":150,
                  "probabilityRepeatWhenWrong":0,
                  "averageReturnCriterion":0.8, 
                  "minTrialsCriterion":5,
                  "sampleSampleWithReplacement":True,
                  "drawEyeFixationDot":True
                  }]

    ENVIRONMENT = {
                    'playspace_degreesVisualAngle':24,
                    'playspace_verticalOffsetInches':0, 
                    'playspace_viewingDistanceInches':8, 
                    'screen_virtualPixelsPerInch':143.755902965,
                    'primary_reinforcer_type':'juice', 
                    'action_event_type':['mouseup', 'touchstart', 'touchmove'],
                    'rigEnvironment':'monkeybox', 
                    "bonusUSDPerCorrect":0.0005,
                    "juiceRewardPer1000Trials":250,


                }  

    SESSION_PACKAGE = {'GAME_PACKAGE':{'IMAGEBAGS':IMAGEBAGS, 'TASK_SEQUENCE':TASK_SEQUENCE, 'GAME':GAME}, 
    'ENVIRONMENT':ENVIRONMENT}
    c.write_landing_page(SESSION_PACKAGE, agentId = 'example_inlab_worker', landingPageName = 'landingPage_InlabMTS.html', saveDirectoryPath = SAVE_LOCATION) 
    return 

def makeInLabSR():
    sessionPackage = '/MonkeyTurk_upstairs/Subjects/exampleSR.json'
    c.write_landing_page(sessionPackage, agentId = 'example_inlab_worker', landingPageName = 'landingPage_InlabSR.html', saveDirectoryPath = SAVE_LOCATION) 
    return

def makeMechanicalTurkSR(): 
    IMAGEBAGS = {"stimulus_objectome_flute":["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_flute_e0aed0e2c3f0c3cb7a7e235bd931f193a536391d_ty-0.85987_tz-0.38018_rxy-36.131_rxz152.6439_ryz28.9932_s1.4314.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_flute_2012a31313faa422b2623460d0c33a9f5eb3b238_ty-0.33547_tz-0.0026731_rxy-38.2159_rxz-115.311_ryz90.0954_s1.3508.png"], 
    "token_objectome_flute": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_flute.png"], 
    "stimulus_objectome_dog": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_dog_e1ed016de5e47e8a6567123ce134d72b7187db73_ty0.43294_tz-0.29943_rxy-112.6794_rxz75.5665_ryz127.211_s1.6328.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_dog_28ebb7db56691da21fa6d640f5ef719f916cb7ff_ty-0.48998_tz-0.20078_rxy-84.7937_rxz-117.8076_ryz175.5429_s1.3151.png"], 
    "token_objectome_dog": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_dog.png"], 
    "token_objectome_pineapple": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_pineapple.png"],
    "stimulus_objectome_pineapple": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_pineapple_5946318bc2cdd1947534ae15d43aa7a0d820506e_ty-0.64759_tz0.33642_rxy-5.6836_rxz-71.4586_ryz62.4466_s1.169.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_pineapple_c50790daa826f1d3fbed5580820c6c91fdded273_ty-0.57074_tz0.84081_rxy-157.3224_rxz64.5421_ryz167.7568_s0.86084.png"]
    }

    GAME = {'gameId':'example_MechanicalTurk_SR',
            "periodicRewardIntervalMsec":0,
            "periodicRewardAmount":0,
            "onFinish":"continue",
            "minimumTrials":2,
            "maximumTrials":800,
    }

    TASK_SEQUENCE = [{
                    "taskType":"SR", 
                    "sampleBagNames":['stimulus_objectome_pineapple', 'stimulus_objectome_flute'], 
                    "fixationXCentroid":0.5,
                    "fixationYCentroid":0.8,
                    "fixationDiameterDegrees":3,
                    "sampleXCentroid":0.5,
                    "sampleYCentroid":0.5,
                    "sampleDiameterDegrees":8,
                    "actionXCentroid":[0.3, 0.7], 
                    "actionYCentroid":[0.8, 0.8],
                    "actionDiameterDegrees":[6, 6],
                    "choiceXCentroid":[0.3, 0.7],
                    "choiceYCentroid":[0.8, 0.8],
                    "choiceDiameterDegrees":[4, 4],
                    "rewardMap":{'stimulus_objectome_pineapple':[1, 0], 'stimulus_objectome_flute':[0, 1]},
                    "sampleOnMsec":200, 
                    "sampleOffMsec":0,
                    "choiceTimeLimitMsec":5000,
                    "punishTimeOutMsec":400,
                    "punishStreakTimeOutMultiplier":1.2,
                    "rewardTimeOutMsec":150,
                    "probabilityRepeatWhenWrong":0,
                    "averageReturnCriterion":0.8, 
                    "minTrialsCriterion":5,
                    "sampleSampleWithReplacement":False,
                    "drawEyeFixationDot":True
                    }]

    GAME_PACKAGE = {'IMAGEBAGS':IMAGEBAGS, 'GAME':GAME, 'TASK_SEQUENCE':TASK_SEQUENCE}
    ENVIRONMENT = {
                      'playspace_degreesVisualAngle':24,
                      'playspace_verticalOffsetInches':0, 
                      'playspace_viewingDistanceInches':8, 
                      'screen_virtualPixelsPerInch':143.755902965,
                      'primary_reinforcer_type':'monetary', 
                      'action_event_type':['mouseup', 'touchstart', 'touchmove'],
                      'rigEnvironment':'mechanicalturk', 
                      "bonusUSDPerCorrect":0.0005,
                      "juiceRewardPer1000Trials":250, 
                      "instructionsDialogueString":"<ul><p><text style=\"font-weight:bold; font-size:large\">Thank you for your interest and contributing to research at at MIT!</text><pi><li>Please use the latest version of <b>Google Chrome</b> to work on this HIT. It may not work correctly on other browsers.<p><li>You will be presented with rapidly flashed images. <b>Your task is to figure out where to click on parts of the screen based on the information in the images.</b><p><li>The sound of a bell means you did something right, and received a small bonus reward.<p><li>Each trial begins with a <b>WHITE DOT</b>. Click the dot to begin the trial.<p><li>The HIT will submit <b>AUTOMATICALLY</b> after a certain number of trials. If the HIT freezes or does not submit, please contact us to resolve the issue and receive compensation for your time.<p><text style=\"color:#7A7A7A; font-size:smaller; font-style:italic\">If you cannot meet these requirements or if doing so could cause discomfort or injury, do not accept this HIT. You will not be penalized in any way.</text></ul>"
                  }   

    sessionPackage = {'GAME_PACKAGE':GAME_PACKAGE, 'ENVIRONMENT':ENVIRONMENT}
    c.write_landing_page(sessionPackage, agentId = None, landingPageName = 'landingPage_MechanicalTurkSR.html', saveDirectoryPath = SAVE_LOCATION) 

    
    return


def makeMechanicalTurkMTS(): 

    IMAGEBAGS = {"stimulus_objectome_flute":["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_flute_e0aed0e2c3f0c3cb7a7e235bd931f193a536391d_ty-0.85987_tz-0.38018_rxy-36.131_rxz152.6439_ryz28.9932_s1.4314.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_flute_2012a31313faa422b2623460d0c33a9f5eb3b238_ty-0.33547_tz-0.0026731_rxy-38.2159_rxz-115.311_ryz90.0954_s1.3508.png"], 
    "token_objectome_flute": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_flute.png"], 
    "stimulus_objectome_dog": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_dog_e1ed016de5e47e8a6567123ce134d72b7187db73_ty0.43294_tz-0.29943_rxy-112.6794_rxz75.5665_ryz127.211_s1.6328.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_dog_28ebb7db56691da21fa6d640f5ef719f916cb7ff_ty-0.48998_tz-0.20078_rxy-84.7937_rxz-117.8076_ryz175.5429_s1.3151.png"], 
    "token_objectome_dog": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_dog.png"], 
    "token_objectome_pineapple": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_pineapple.png"],
    "stimulus_objectome_pineapple": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_pineapple_5946318bc2cdd1947534ae15d43aa7a0d820506e_ty-0.64759_tz0.33642_rxy-5.6836_rxz-71.4586_ryz62.4466_s1.169.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_pineapple_c50790daa826f1d3fbed5580820c6c91fdded273_ty-0.57074_tz0.84081_rxy-157.3224_rxz64.5421_ryz167.7568_s0.86084.png"]
    }

    GAME = {'gameId':'example_MechanicalTurk_MTS',
            "periodicRewardIntervalMsec":0,
            "periodicRewardAmount":0,
            "onFinish":"continue",
            "minimumTrials":2,
            "maximumTrials":800,
    }

    TASK_SEQUENCE = [{
                    "taskType":"MTS", 
                    "sampleBagNames":['stimulus_objectome_pineapple', 'stimulus_objectome_flute'], 
                    "fixationXCentroid":0.5,
                    "fixationYCentroid":0.8,
                    "fixationDiameterDegrees":3,
                    "sampleXCentroid":0.5,
                    "sampleYCentroid":0.5,
                    "sampleDiameterDegrees":8,
                    "actionXCentroid":[0.3, 0.7], 
                    "actionYCentroid":[0.8, 0.8],
                    "actionDiameterDegrees":[6, 6],
                    "choiceXCentroid":[0.3, 0.7],
                    "choiceYCentroid":[0.8, 0.8],
                    "choiceDiameterDegrees":[4, 4],
                    "choiceMap":{"stimulus_objectome_flute":"token_objectome_flute", 
                    "stimulus_objectome_pineapple":"token_objectome_pineapple", 
                    'stimulus_objectome_dog':"token_objectome_dog"}, 
                    "sampleOnMsec":200, 
                    "sampleOffMsec":0,
                    "choiceTimeLimitMsec":5000,
                    "punishTimeOutMsec":400,
                    "punishStreakTimeOutMultiplier":1.2,
                    "rewardTimeOutMsec":150,
                    "probabilityRepeatWhenWrong":0,
                    "averageReturnCriterion":0.8, 
                    "minTrialsCriterion":5,
                    "sampleSampleWithReplacement":False,
                    "drawEyeFixationDot":True
                    }]

    GAME_PACKAGE = {'IMAGEBAGS':IMAGEBAGS, 'GAME':GAME, 'TASK_SEQUENCE':TASK_SEQUENCE}
    ENVIRONMENT = {
                      'playspace_degreesVisualAngle':24,
                      'playspace_verticalOffsetInches':0, 
                      'playspace_viewingDistanceInches':8, 
                      'screen_virtualPixelsPerInch':143.755902965,
                      'primary_reinforcer_type':'monetary', 
                      'action_event_type':['mouseup', 'touchstart', 'touchmove'],
                      'rigEnvironment':'mechanicalturk', 
                      "bonusUSDPerCorrect":0.0005, 
                      "juiceRewardPer1000Trials":250, 
                      "instructionsDialogueString":"<ul><p><text style=\"font-weight:bold; font-size:large\">Thank you for your interest and contributing to research at at MIT!</text><pi><li>Please use the latest version of <b>Google Chrome</b> to work on this HIT. It may not work correctly on other browsers.<p><li>You will be presented with rapidly flashed images. <b>Your task is to match images with the one that was rapidly flashed (this will become clear after you try a few trials).</b><p><li>The sound of a bell means you did something right, and received a small bonus reward.<p><li>Each trial begins with a <b>WHITE DOT</b>. Click the dot to begin the trial.<p><li>The HIT will submit <b>AUTOMATICALLY</b> after a certain number of trials. If the HIT freezes or does not submit, please contact us to resolve the issue and receive compensation for your time.<p><text style=\"color:#7A7A7A; font-size:smaller; font-style:italic\">If you cannot meet these requirements or if doing so could cause discomfort or injury, do not accept this HIT. You will not be penalized in any way.</text></ul>"
                  }   

    sessionPackage = {'GAME_PACKAGE':GAME_PACKAGE, 'ENVIRONMENT':ENVIRONMENT}
    c.write_landing_page(sessionPackage, agentId = None, landingPageName = 'landingPage_MechanicalTurkMTS.html', saveDirectoryPath = SAVE_LOCATION) 
    return 


def makeMechanicalTurkSwitcher(): 

    IMAGEBAGS = {"stimulus_objectome_flute":["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_flute_e0aed0e2c3f0c3cb7a7e235bd931f193a536391d_ty-0.85987_tz-0.38018_rxy-36.131_rxz152.6439_ryz28.9932_s1.4314.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_flute_2012a31313faa422b2623460d0c33a9f5eb3b238_ty-0.33547_tz-0.0026731_rxy-38.2159_rxz-115.311_ryz90.0954_s1.3508.png"], 
    "token_objectome_flute": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_flute.png"], 
    "stimulus_objectome_dog": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_dog_e1ed016de5e47e8a6567123ce134d72b7187db73_ty0.43294_tz-0.29943_rxy-112.6794_rxz75.5665_ryz127.211_s1.6328.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_dog_28ebb7db56691da21fa6d640f5ef719f916cb7ff_ty-0.48998_tz-0.20078_rxy-84.7937_rxz-117.8076_ryz175.5429_s1.3151.png"], 
    "token_objectome_dog": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_dog.png"], 
    "token_objectome_pineapple": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome_tokens/images/objectomeTokens_objectome_pineapple.png"],
    "stimulus_objectome_pineapple": ["https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_pineapple_5946318bc2cdd1947534ae15d43aa7a0d820506e_ty-0.64759_tz0.33642_rxy-5.6836_rxz-71.4586_ryz62.4466_s1.169.png", "https://s3.amazonaws.com/milresources/Images/MonkeyTurkSets/objectome/images/objectome_pineapple_c50790daa826f1d3fbed5580820c6c91fdded273_ty-0.57074_tz0.84081_rxy-157.3224_rxz64.5421_ryz167.7568_s0.86084.png"]
    }

    GAME = {'gameId':'example_MechanicalTurk_MTS_to_SR',
            "periodicRewardIntervalMsec":0,
            "periodicRewardAmount":0,
            "onFinish":"loop",
            "minimumTrials":30,
            "maximumTrials":30,
    }

    TASK_SEQUENCE = [{
                    "taskType":"MTS", 
                    "sampleBagNames":['stimulus_objectome_pineapple', 'stimulus_objectome_flute'], 
                    "fixationXCentroid":0.5,
                    "fixationYCentroid":0.8,
                    "fixationDiameterDegrees":3,
                    "sampleXCentroid":0.5,
                    "sampleYCentroid":0.5,
                    "sampleDiameterDegrees":8,
                    "actionXCentroid":[0.3, 0.7], 
                    "actionYCentroid":[0.8, 0.8],
                    "actionDiameterDegrees":[6, 6],
                    "choiceXCentroid":[0.3, 0.7],
                    "choiceYCentroid":[0.8, 0.8],
                    "choiceDiameterDegrees":[4, 4],
                    "choiceMap":{"stimulus_objectome_flute":"token_objectome_flute", 
                    "stimulus_objectome_pineapple":"token_objectome_pineapple", 
                    'stimulus_objectome_dog':"token_objectome_dog"}, 
                    "sampleOnMsec":200, 
                    "sampleOffMsec":0,
                    "choiceTimeLimitMsec":5000,
                    "punishTimeOutMsec":400,
                    "punishStreakTimeOutMultiplier":1.2,
                    "rewardTimeOutMsec":150,
                    "probabilityRepeatWhenWrong":0,
                    "averageReturnCriterion":0.8, 
                    "minTrialsCriterion":5,
                    "sampleSampleWithReplacement":False,
                    "drawEyeFixationDot":True
                    }, 
                    {
                    "taskType":"SR", 
                    "sampleBagNames":['stimulus_objectome_pineapple', 'stimulus_objectome_flute'], 
                    "fixationXCentroid":0.5,
                    "fixationYCentroid":0.8,
                    "fixationDiameterDegrees":3,
                    "sampleXCentroid":0.5,
                    "sampleYCentroid":0.5,
                    "sampleDiameterDegrees":8,
                    "actionXCentroid":[0.3, 0.7], 
                    "actionYCentroid":[0.8, 0.8],
                    "actionDiameterDegrees":[6, 6],
                    "choiceXCentroid":[0.3, 0.7],
                    "choiceYCentroid":[0.8, 0.8],
                    "choiceDiameterDegrees":[4, 4],
                    "rewardMap":{"stimulus_objectome_flute":[0, 1], 
                    "stimulus_objectome_pineapple":[1, 0]}, 
                    "sampleOnMsec":200, 
                    "sampleOffMsec":0,
                    "choiceTimeLimitMsec":5000,
                    "punishTimeOutMsec":400,
                    "punishStreakTimeOutMultiplier":1.2,
                    "rewardTimeOutMsec":150,
                    "probabilityRepeatWhenWrong":0,
                    "averageReturnCriterion":0.8, 
                    "minTrialsCriterion":5,
                    "sampleSampleWithReplacement":False,
                    "drawEyeFixationDot":True
                    }]

    GAME_PACKAGE = {'IMAGEBAGS':IMAGEBAGS, 'GAME':GAME, 'TASK_SEQUENCE':TASK_SEQUENCE}
    ENVIRONMENT = {
                      'playspace_degreesVisualAngle':24,
                      'playspace_verticalOffsetInches':0, 
                      'playspace_viewingDistanceInches':8, 
                      'screen_virtualPixelsPerInch':143.755902965,
                      'primary_reinforcer_type':'monetary', 
                      'action_event_type':['mouseup', 'touchstart', 'touchmove'],
                      'rigEnvironment':'mechanicalturk', 
                      "bonusUSDPerCorrect":0.0005, 
                      "juiceRewardPer1000Trials":250, 
                      "instructionsDialogueString":"<ul><p><text style=\"font-weight:bold; font-size:large\">Thank you for your interest and contributing to research at at MIT!</text><pi><li>Please use the latest version of <b>Google Chrome</b> to work on this HIT. It may not work correctly on other browsers.<p><li>You will be presented with rapidly flashed images. <b>Your task is to figure out where to click on parts of the screen based on the information in the images.</b><p><li>The sound of a bell means you did something right, and received a small bonus reward.<p><li>Each trial begins with a <b>WHITE DOT</b>. Click the dot to begin the trial.<p><li>The HIT will submit <b>AUTOMATICALLY</b> after a certain number of trials. If the HIT freezes or does not submit, please contact us to resolve the issue and receive compensation for your time.<p><text style=\"color:#7A7A7A; font-size:smaller; font-style:italic\">If you cannot meet these requirements or if doing so could cause discomfort or injury, do not accept this HIT. You will not be penalized in any way.</text></ul>"
                  }   

    sessionPackage = {'GAME_PACKAGE':GAME_PACKAGE, 'ENVIRONMENT':ENVIRONMENT}
    c.write_landing_page(sessionPackage, agentId = None, landingPageName = 'landingPage_MechanicalTurkMTS_to_SR.html', saveDirectoryPath = SAVE_LOCATION) 
    return 


if __name__ == '__main__': 
    makeInLabMTS()
    makeInLabSR()
    makeMechanicalTurkSR()
    makeMechanicalTurkMTS()
    makeMechanicalTurkSwitcher()
