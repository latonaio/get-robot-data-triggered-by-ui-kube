# get-robot-data-triggered-by-ui

・UIから渡されたデータ収集開始、終了トリガを処理する

・get-robot-data-from-yaskawa:featurer/reload-command-listのcommand_list.jsonを更新する


### input

・add_listに収集を開始したいデータのコマンド番号と配列番号を入れて渡す

・remove_listに収集を終了したいデータのコマンド番号と配列番号を入れて渡す

・片方だけでも両方同時でも機能する

```
    "metadata": [
        {
    	    "key":"add_list",
            "value": [
    	        {
                    "command": "78",
                    "arrayNo": [
                        "5001",
                        "6001"
                    ]
                },
                {
                    "command": "7f",
                    "arrayNo": [
                        "3",
                        "4"
                    ]
                }
            ]
        },
        {
    	    "key":"remove_list",
            "value": [
    	        {
                    "command": "78",
                    "arrayNo": [
                        "7001",
                        "8001"
                    ]
                },
                {
                    "command": "7f",
                    "arrayNo": [
                        "126",
                        "127"
                    ]
                }
            ]
        }
    ]
```

### output

・特になし
