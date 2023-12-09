import yiyanAPI
from audioReco import sReco
from audioReco import sr
from tts import say

greet = "hello"

def beginConversa():
    while True:
        said = listen_trans(sReco,10)
        if said.isspace() or said is None:
            return
        elif "彻底关闭" in said and len(said)<10:
            return False
        elif isEnd(said):
            break
        else:
            if '详' in said:
                say( yiyanAPI.yiyanRequest(said) )
                # say("这是详解")
            else:
                say( yiyanAPI.yiyanRequest(said))
                # say("这是简答")
    return True

def formalResult(resu):
    return "{\n  \"text\" : \"" + resu + "\"\n}"

def informalResult(resu):
    if resu.count('"') < 4:
        return "Not enough quotes in the string"
    start = resu.index('"', resu.index('"', resu.index('"') + 1) + 1) + 1
    end = resu.index('"', start)
    return resu[start:end]

def listen_trans(recognizer_instance, time = None):
    print("start recognize")
    with sr.Microphone() as source:
        audioData = recognizer_instance.listen(source,time)
    result = informalResult( recognizer_instance.recognize_vosk(audioData) )
    print("I think you said: ", result)
    return result

def isEnd(said):
    endWords = ['再见', '谢谢', '结束', '关闭', '到此为止', '停']
    for word in endWords:
        if word in said and len(said)<6:
            return True
    return False



if __name__ == '__main__':
    print("start working")
    isMultAskBegin = False
    #icon = createIconStray()

    while True:
        print("wait hello")
        said = listen_trans(sReco)
        if greet in said and len(said) <10:
            say("你好")
            if beginConversa() == False:
                break
        elif "彻底" in said and "关闭" in said and len(said) < 10:
            break

    say("再见")
    print("over")

