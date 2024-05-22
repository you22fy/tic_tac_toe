# python tic tac toe

## 概要

python で作成した GUI で遊べる CPU 対戦三目並べゲームです。

## 実行方法

このプログラムは`Python 3.11.6`で動作することを確認しています。それ以外のバージョンでの動作は保証しません。
また以下の動作確認では以下のことができている前提で説明を行います。

- python 環境の構築(以下の二つのどちらかを想定しています)
  - poetry が実行可能な環境
  - pip が実行可能な環境
- git のインストール

### 1. リポジトリのクローン

```zsh
git clone https://github.com/you22fy/tic_tac_toe.git
cd tic_tac_toe
```

### 2. 実行の準備

#### poetry を使用する場合

```zsh
poetry install
```

#### pip を使用する場合

```zsh
pip install -r requirements.txt
```

### 3. 実行

#### poetry を使用する場合

```zsh
poetry run python python_tic_tac_toe/main.py
```

#### pip を使用する場合

```zsh
python python_tic_tac_toe/main.py
```

### 4. 楽しむ

- ゲームが開始されるので、CPU と対戦してください。
- CPU は開いてるマスからランダムに１つ選んで手をうつようになっています。
  - CPU の挙動を変更して、より強くすることも可能です。(future work)

## 使用技術
- python 3.11.6
- tkinter
- poetry

## mermaid 図

プログラム全体のフローチャートとシーケンス図を以下に示します。

### フローチャート

```mermaid
flowchart TD
    start(ゲーム開始) --> init[ゲーム初期化]
    init --> human_turn{人間のターン}

    human_turn --> human_move[人間が手を選択]
    human_move --> update_board1[盤面更新]
    update_board1 --> check_winner1{勝利判定}

    check_winner1 --> |勝者なし|cpu_turn[CPUのターン]
    check_winner1 --> |勝者ありまたは引き分け|show_winner[勝利ダイアログ表示]
    show_winner --> game_end[ゲーム終了]

    cpu_turn --> cpu_move[CPUが手を選択]
    cpu_move --> update_board2[盤面更新]
    update_board2 --> check_winner2{勝利判定}

    check_winner2 --> |勝者なし|human_turn
    check_winner2 --> |勝者ありまたは引き分け|show_winner

```

### シーケンス図

```mermaid
sequenceDiagram
    participant Player as player
    participant System as system
    participant CPU as CPU-player

    Player->>+System: ゲームを開始
    loop ゲームの進行
        Note over Player,CPU: 盤面の状態を確認
        Player->>+System: 手を選択
        System->>-Player: 盤面を更新
        System->>System: 勝利判定
        alt 勝利または引き分け
            System->>Player: 勝利/引き分けダイアログを表示
            Player->>System: ゲームを終了
        else 勝者なし
            System->>+CPU: CPUのターン
            CPU->>-System: 手を選択
            System->>System: 盤面を更新
            System->>System: 勝利判定
            alt 勝利または引き分け
                System->>Player: 勝利/引き分けダイアログを表示
                Player->>System: ゲームを終了
            else 勝者なし
                Note right of System: ターン終了、プレイヤーのターンへ
            end
        end
    end

```
