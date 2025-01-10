# 数あてゲーム / Guess The Number Game

## 目次 / Table of Contents
- [日本語 (Japanese)](#日本語-japanese)
- [English](#english)

---

## 日本語 (Japanese)
![遊び始めの様子](game_image_ja.png)

### ゲーム概要
数あてゲームは、プレイヤーが指定した整数の範囲から、コンピュータがランダムに選んだ数を当てるシンプルなゲームです。

### 特徴
- 任意の整数範囲を設定可能
- プレイ内容を基にしたスコア評価
- ハイスコアランキング機能付き
- ランキングデータは自動保存（ローカル環境に保存）
- 日本語・英語対応のメッセージ

### インストール手順
1. **Python3.8以上をインストール**:
   必要に応じて、公式サイトからPythonをダウンロード、インストールしてください。

2. **リポジトリのクローン**:
   ターミナルを起動して、次のコマンドを実行して、ゲームを取得します。
    ```bash
    git clone https://github.com/akemashita/GuessTheNumberGame.git
    ```

3. **ファイルの実行**:
   次のコマンドを実行して、クローンしたフォルダに移動、ゲームファイルを実行します。
    ```bash
    cd GuessTheNumberGame
    python3 app.py
    ```

### 遊び方
1. **言語の選択**:
   ゲーム開始時に言語選択画面が表示されます。選択がなければ日本語がデフォルトとなります。

2. **範囲の設定**:
   メッセージに従い、推測する整数範囲を設定します。（例: 2, 10）

3. **ゲームの進行**:
   - 画面に表示されるヒントをもとに数を推測します。
   - 推測が正解するまで続けます。

4. **ゲーム終了**:
   途中で終了したい場合は、`Ctrl + C` を押してください。

### スコア評価について
ゲーム終了時、スコアが計算されます。

#### 計算式
スコアは以下の式で算出されます：
`スコア = (理想的な試行数 / 実際の試行数) × 倍率`

#### 詳細
- **理想的な試行数**: `ceil(log2(要素数))`
- **要素数**: `設定範囲の終わりの数 - 設定範囲の初めの数 + 1`

#### 倍率
倍率は要素数に基づいて次のように決まります：
- 要素数が 1000 以上の場合: **10,000**
- 要素数が 100 以上 1000 未満の場合: **5,000**
- 要素数が 50 以上 100 未満の場合: **2,500**
- 要素数が 50 未満の場合: **100**

---

## English
![Image of the beginning of play](game_image_en.png)


### Game Overview
"Guess the Number" is a simple game where the player tries to guess a random number selected by the computer within a specified range.

### Features
- Set any integer range for guessing.
- Score evaluation based on gameplay.
- High score ranking feature.
- Ranking data is automatically saved (locally stored).
- Supports both Japanese and English messages.

### Installation Instructions
1. Install Python 3.8 or later:
Download and install Python from the official website if needed.

2. Clone the repository:
Open your terminal and execute the following command to obtain the game:
    ```bash
    git clone https://github.com/akemashita/GuessTheNumberGame.git
    ```

3. Run the game:
Navigate to the cloned folder and execute the game file with the following commands:

    ```bash
    cd GuessTheNumberGame
    python3 app.py
    ```

### How to Play
1. Select a language:
At the start of the game, a language selection screen will be displayed. If no selection is made, Japanese will be used by default.

2. Set the range:
Follow the messages to set the range of integers for guessing (e.g. 2, 10).

3. Gameplay:
- Guess the number based on the hints displayed on the screen.
- Continue guessing until you find the correct answer.

4. End the game:
To exit the game prematurely, press Ctrl + C.

### About Score Evaluation
At the end of the game, your score will be calculated.

#### Formula
The score is calculated using the following formula:
`Score = (Ideal attempts / Actual attempts) × Multiplier`

#### Details
- Ideal attempts: `ceil(log2(Number of elements))`
- Number of elements: `End of the range - Start of the range + 1`

#### Multiplier
The multiplier is determined based on the number of elements in the range:

- For 1000 or more elements: 10,000
- For 100 to 999 elements: 5,000
- For 50 to 99 elements: 2,500
- For fewer than 50 elements: 100