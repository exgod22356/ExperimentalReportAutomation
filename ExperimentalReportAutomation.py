import random
import time
#random.seed(13)

FirstFart = [
    "这次的学习使我受益匪浅。",
    "这次的学习让我收获了很多。",
    "这次课程的学习增进了我对这门课程的认识。",
    "这门课的学习提高了我对这门课的理解。",
    "这门课程的学习增加了我对这门课程的理解。"
    "这次课程的学习让我学到了很多东西，让我从最初的一无所知到我逐渐有能力来完成这门课程。",
    "这次的学习拓宽了我的视野，让我了解到了更多。",
    "通过这次课程，我明白了很多东西。"
]
TopSentences = [
    "它让我了解到了与{}有关的各种知识。",
    "它加深了我对{}的理解，使我对它的认知更为深刻了。",
    "它让我更加扎实地掌握了{}的相关知识。"
]
CommonFart = [
    "学习{}并不是一项简单的事，但是也并不困难，只是需要为此付出精力。",
    "{}的学习让我暴露了许多我对于相关知识的不足之处，让我补足了许多。",
    "我在这门课程中实质地接触到了，了解到了{}的本质。",
    "对{}的学习让我认识到了更多的东西。",
    "我充分了解了{}的本质。",
    "学以致用，这门课程提高了我的动手能力，培养了我对{}的认知，对前面实验所掌握的知识和技能也起到了一个很好的复习和锻炼。",
    "我对{}相关知识的掌握得到了进一步的强化。",
    "我对{}的兴趣得到了提高，这也让我更多相关理论知识。"
]
TransitionFart = [
    "我自己在这次的学习中，得到的不仅是知识，更有能力的提升。",
    "在学习中我复习了许多之前的知识，这帮助我巩固了许多。",
    "课程比我与我想象中有所不同，但也确实让我了解到了很多。"

]
QuestionFart = [
    "在课程学习过程中我遇到了很多困难，但是通过上网查阅资料很好的解决了问题。",
    "这次的学习中我遇到了很多问题，随着自己的一步步解决，自身的能力也得到了提高，也使我更有动力继续下面的学习。",
    "这次课程中有许多东西相对而言比较复杂，也比较难懂，但经过查阅资料，我最终还是克服了这些困难。"

]
EndingFart = [
    "这次的内容总体来说不算困难，但是要熟练掌握{}的相关知识，我还要继续学习，继续钻研。",
    "这次的内容总而言之让我学到了许多，相信在将来我能将{}的相关知识更多地运用于实际生活中去，发挥更大的作用。",
    "总而言之，这次我学到了很多东西。这让我相信，在将来，我能够在现实生活中更多地运用{}的相关知识，并发挥更大的作用。",
    "总而言之，这次的实验使我对{}有了很好的了解，在将来我还需要继续的学习，更好地掌握这门知识。",
    "总的来说这次收获挺多。在将来，我还需要继续学习{},以更好地掌握相关知识",
    "总之，这次对{}的学习，让我收获了不少。"
]
while True:
    random.shuffle(FirstFart)
    random.shuffle(TopSentences)
    random.shuffle(CommonFart)
    random.shuffle(TransitionFart)
    random.shuffle(QuestionFart)
    random.shuffle(EndingFart)

    teststr = input()
    articlelis = []
    articlelis.append(FirstFart[0])
    articlelis.append(TopSentences[0].format(teststr))
    articlelis.append(CommonFart[0].format(teststr))
    articlelis.append(QuestionFart[0])
    articlelis.append(TransitionFart[0])
    articlelis.append(CommonFart[1].format(teststr))
    articlelis.append(EndingFart[0].format(teststr))
    article = ""
    for i in articlelis:
        article+=i

    print(article)
