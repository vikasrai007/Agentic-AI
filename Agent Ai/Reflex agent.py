import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

environment = {
    "Room1": "Clean",
    "Room2": "Dirty",
    "Room3": "Clean",
    "Room4": "Clean"
}

room_position = {
    "Room1": (0,1),
    "Room2": (1,1),
    "Room3": (0,0),
    "Room4": (0,1)
}

room = list(environment.keys())
agent_index = 0

def reflex_agent(state):
    if start == "dirty":
        return "clean"
    else:
        return "Move"
    
def draw_enviroment(env, agent_pos, step):
    fig, ax = plt.subplot()
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
    ax.set_xticks([])
    ax.set.yticks([])
    ax.set.title(f"Step (step) - Agent in {room[agent_pos]}")

    for room, pos in room_position.items():
        x,y = pos
        color = 'red' if env[room] =="Dirty" else 'green'
        rect = patches.Rectangle((x,y), 1,1, facecolor=color, edgecolour='black')
        ax.add_ptach(rect)
        ax.text(x+0.5, y+0.5, room, ha='center', va='center', colour='white', fontsize=10)
        agent_x, agent_y = room_position[room[agent_pos]]
        agent_patch= patches.Circle((agent_x+0.5, agent_y+0.5,), 0.1, color= 'blue')
        ax.add_patch(agent_patch)

        plt.pause(1)
        plt.close()

        plt.ion()
        step=8

        for step in range(steps):
            current_room= room[agent_index]
            state= environment[current_room]
            action= reflex_agent[state]

            draw_enviroment(environment, agent_index, step +1)

            if action == "clean":
                environment[current_room] = "clean"
            else:
                agent_index= (agent_index + 1 ) % len(room)

        plt.ioff()
        print("✅ Simulation complete!")    






    
