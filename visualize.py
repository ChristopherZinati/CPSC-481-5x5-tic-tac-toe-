import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('simulation_results.csv')

    for opponent in df['opponent'].unique():
        sub = df[df['opponent'] == opponent]

        plt.figure()
        plt.plot(sub['depth'], sub['X_wins'], marker='o', label='X wins')
        plt.plot(sub['depth'], sub['O_wins'], marker='o', label='O wins')
        plt.plot(sub['depth'], sub['Draws'], marker='o', label='Draws')
        plt.xlabel('Search Depth')
        plt.ylabel('Game Count')
        plt.title(f'Win/Tie Counts vs {opponent.capitalize()} Bot')
        plt.legend()
        plt.show()

        plt.figure()
        plt.plot(sub['depth'], sub['Pruned'], marker='o', label='Branches pruned')
        plt.xlabel('Search Depth')
        plt.ylabel('Pruned Branches')
        plt.title(f'Pruning vs {opponent.capitalize()} Bot')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    main()
