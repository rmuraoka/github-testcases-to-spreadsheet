# github-testcases-to-spreadsheet
Githubで書いたテストケースをGoogleスプレッドシートに展開します。 Integrate test cases written on GitHub with Google Spreadsheets.
## 事前準備
1. Googleスプレッドシートを作成し、適切な形式でカラムを設定します。 
2. Google Cloud Platformでプロジェクトを作成し、Google Sheets APIを有効にします。
3. API認証用のサービスアカウントを作成し、必要なスコープを持つ認証情報をダウンロードします。
4. このリポジトリをクローンし、取得した情報をGitHubリポジトリのSecretsに追加します。
   1. `GOOGLE_CREDENTIALS`：3. で取得したjson形式の認証情報
   2. `SPREADSHEET_ID`: 1.で作成したスプレッドシートのID
   3. `WORKSHEET_TITLE`: 1.で作成したスプレッドシートの、テストケースを書き込みたいシート名
## 実行手順
1. testcasesディレクトリ以下にテストケースをpushすると自動的にGithub Actionsがトリガーされ、指定したスプレッドシートのワークシートにテストケースが連携されます。
2. 実行管理などを行う場合は適宜プルダウンなどを追加してください。
## サポート
うまく動作しない場合はIssueを立てて教えてください。
## Preliminary Setup
1. Create a Google Spreadsheet and set up columns in the appropriate format.
2. Create a project on Google Cloud Platform and enable the Google Sheets API.
3. Create a service account for API authentication and download credentials with the necessary scopes.
4. Clone this repository and add the obtained information to the Secrets of the GitHub repository.
    1. `GOOGLE_CREDENTIALS`：The JSON-formatted authentication credentials obtained in step 3.
    2. `SPREADSHEET_ID`: The ID of the spreadsheet created in step 1.
    3. `WORKSHEET_TITLE`: The name of the sheet in the spreadsheet created in step 1, where you want to write the test cases.
## Execution Procedure
1. When test cases are pushed to the testcases directory, GitHub Actions will be triggered automatically, integrating the test cases with the designated worksheet in the spreadsheet.
2. If you need to manage executions, please add dropdowns or similar as necessary.
## Support
If it does not work properly, please raise an issue to let me know.
