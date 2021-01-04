quest = ['Quest 1', 'Quest 2', 'Quest 3']
quest_tuple = quest.copy()  # same list but can`t edit element


def printQuest(quests):
    print(len(quests))

    for q in quests:
        print(q)

    print('*****************************************************')

    i = 1
    while i <= len(quests):
        print(quests[i - 1])
        i += 1


if __name__ == "__main__":
    quest.append('Quest 4')  # add element to last index of list
    quest.insert(0, 'Quest 0')  # add element to index position of list
    quest.remove('Quest 4')  # remove element of list

    printQuest(quest)
    print(quest_tuple)
