import matplotlib.pyplot as plt

mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]

raj_parties = ['INC', 'BJP', 'BSP', 'Others']
raj_seats = [69, 115, 2, 13]

mp_total_seats = sum(mp_seats)
raj_total_seats = sum(raj_seats)

fig, axs = plt.subplots(1, 2, figsize=(14, 7))

axs[0].pie(mp_seats, labels=mp_parties, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0, 0])
axs[0].set_title('Madhya Pradesh - Seat Share')
axs[0].axis('equal') 
axs[1].pie(raj_seats, labels=raj_parties, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0, 0])
axs[1].set_title('Rajasthan - Seat Share')
axs[1].axis('equal') 
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.35

index = range(len(mp_parties))

mp_bars = ax.bar(index, mp_seats, bar_width, label='Madhya Pradesh', color='b')
raj_bars = ax.bar([p + bar_width for p in index], raj_seats, bar_width, label='Rajasthan', color='r')

ax.set_xlabel('Party')
ax.set_ylabel('Seats Won')
ax.set_title('Seats Won by Each Party in Madhya Pradesh and Rajasthan')
ax.set_xticks([p + bar_width / 2 for p in index])
ax.set_xticklabels(mp_parties) 
ax.legend()

plt.tight_layout()
plt.show()
