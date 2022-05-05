# 문제 설명
Given a text file file.txt that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

-c : 매칭을 위한 패턴을 전달
\ : 변수 기호를 문자열로 인식시키기 위해 사용
^ : 문장의 시작을 뜻함
$ : 라인의 끝을 표시
{n} : 앞 문자가 n번 일치해야함
