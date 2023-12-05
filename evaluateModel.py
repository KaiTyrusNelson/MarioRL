def evaluate(name, numEpisodes):
    f = open(name+"_win_rate", "a")
    modelNumber = 460000
    for i in range(5):
        model = PPO.load(name+"/best_model_" + str(modelNumber + i*10000) + ".zip")
        state = env.reset()
        done = False
        plays = 0
        wins = 0
        while plays < numEpisodes:
            if done:
                state = env.reset() 
                if info[0]["flag_get"]:
                    wins +=1
                plays += 1
                print(plays)
            action, _ = model.predict(state)
            state, reward, done, info = env.step(action)
        
        print("Model " + str(modelNumber + i*10000) + " win rate: " + str(wins/(numEpisodes/100)) + "%")
        f.write("Model " + str(modelNumber + i*10000) + " win rate: " + str(wins/(numEpisodes/100)) + "%\n")