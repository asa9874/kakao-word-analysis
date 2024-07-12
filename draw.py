import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = 'C:/Windows/Fonts/malgun.ttf'  # 사용할 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

def drawgraph(human, data):
    num_people = len(human)
    num_cols = 2  # 2열로 그래프를 나타내기 위한 설정
    num_rows = (num_people + num_cols - 1) // num_cols  # 적절한 행 개수 계산
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 4 * num_rows))

    if num_people == 1:
        axes = [axes]  # 하나의 사람일 경우를 처리

    for i, human_name in enumerate(human):
        row = i // num_cols
        col = i % num_cols

        keys = list(data[human_name].keys())
        values = list(data[human_name].values())
        keys_int = [int(key) for key in keys]

        bars = axes[row, col].bar(keys_int, values, color='skyblue')
        axes[row, col].set_xticks(keys_int)
        axes[row, col].set_ylabel('개수')
        axes[row, col].set_title(f'{human_name}')
        axes[row, col].tick_params(axis='x', rotation=45)  # x 축 눈금 라벨 회전 설정

        # 각 막대 위에 개수 표시
        for bar in bars:
            yval = bar.get_height()
            axes[row, col].annotate(f'{yval}', xy=(bar.get_x() + bar.get_width() / 2, yval),
                                    xytext=(0, 3), textcoords='offset points',
                                    ha='center', va='bottom')
        axes[row, col].set_ylim(top=max(values) * 1.1)

    # 남은 빈 그래프 제거
    if num_people % num_cols != 0:
        for i in range(num_people % num_cols, num_cols):
            fig.delaxes(axes[num_rows-1, i])

    # 그래프 간의 간격 조정
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.2, hspace=0.3)
    plt.show()



def drawgraph2(human, data):
    num_people = len(human)
    num_cols = 2  # 2열로 그래프를 나타내기 위한 설정
    num_rows = (num_people + num_cols - 1) // num_cols  # 적절한 행 개수 계산
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 4 * num_rows))

    if num_people == 1:
        axes = [axes]  # 하나의 사람일 경우를 처리

    for i, human_name in enumerate(human):
        row = i // num_cols
        col = i % num_cols

        keys = list(data[human_name].keys())
        values = list(data[human_name].values())
        total = sum(values)
        percentages = [val / total * 100 for val in values]
        keys_int = [int(key) for key in keys]
        
        bars = axes[row, col].bar(keys, percentages, color='skyblue')
        axes[row, col].set_ylabel('백분율(%)')
        axes[row, col].set_xticks(keys_int)
        axes[row, col].set_title(f'{human_name}')
        axes[row, col].tick_params(axis='x', rotation=45)  # x 축 눈금 라벨 회전 설정

        # 각 막대 위에 % 표시
        for bar, percentage in zip(bars, percentages):
            axes[row, col].annotate(f'{percentage:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                                    xytext=(0, 3), textcoords='offset points',
                                    ha='center', va='bottom')
        axes[row, col].set_ylim(top=max(percentages) * 1.1)

    # 남은 빈 그래프 제거
    if num_people % num_cols != 0:
        for i in range(num_people % num_cols, num_cols):
            fig.delaxes(axes[num_rows-1, i])

    # 그래프 간의 간격 조정
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.2, hspace=0.3)
    plt.show()
