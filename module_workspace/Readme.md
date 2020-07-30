# 2020-07-29 RUDA LEE
# SK_infosec - Cloud AI 전문가 과정 교육 

host='localhost' url 정보
user='aiadmin'
password='password'
db='module_db'
docker에서 mysql 실행. port 3306
포트 포워딩 - 이름 : mysql, 호스트IP : 127.0.0.1, 게스트 포트 : 3306

## 테이블 선언은 아래와 같이 수행 됨.
use module_db; 
 
CREATE TABLE member_ (
 	email varchar(50) PRIMARY KEY,
 	name varchar(30),
 	phone_number varchar(20),
 	birthday varchar(20)
 );
ALTER TABLE member_ convert to character set UTF8;

CREATE TABLE club_ (
 	clubID varchar(20) PRIMARY KEY,
 	name varchar(50),
 	phone_number varchar(20),
 	foundation_date varchar(20),
 	address varchar(50)
 );
ALTER TABLE club_ convert to character set UTF8;
 
CREATE TABLE membership_ (
	membershipID varchar(20) PRIMARY KEY,
 	clubID varchar(20),
 	member_email varchar(50),
 	join_date varchar(20),
 	role_in_club varchar(20)
 );
ALTER TABLE membership_ convert to character set UTF8;


## <사용 예시>


가장 기본적이며, 심플한 기능한 간단하게 구현하였습니다.

![image](/uploads/ee9aadc1d7dac161f17b5118870d88ee/image.png)

맨 처음 실행하면 커뮤니티 맴버인지, 클럽 관리자인지 선택한다.


=======================================================================

![image](/uploads/a16fcb43feda0b254f03f4230c2cc6b0/image.png)

![image](/uploads/5a5e086a659d4d6af63879c0576c820a/image.png)

![image](/uploads/978686c2c1db13eff17417df648667d0/image.png)

ID 값(맴버 email/클럽 ID)를 넣고, 없는 사용자이면 entity값을 넣어 등록한다.




=======================================================================

![image](/uploads/fd51e327114ee92982524a82e8f8b4a0/image.png)

![image](/uploads/b797b7823885eeed2876d7f8591f5f79/image.png)

![image](/uploads/fc39283dd4247cd199eda26bda287631/image.png)

등록되어있는 ID 정보로 들어가게 되면, 해당 사용자의 이름으로 메뉴 화면을 띄운다.





=======================================================================

![image](/uploads/4d0e51908ce4cb07da7a13de5aa033bf/image.png)

맴버 메뉴에서 맴버쉽 가입 버튼을 누르면, 현재 가입 가능한 클럽들이 Dict 타입 형태의 list로 출력되며, 해당 clubID를 입력하여 맴버쉽 가입이 가능하다.




=======================================================================

![image](/uploads/e671e83082d4da5a456fdd1465666036/image.png)

![image](/uploads/8ecd7bb5207592705ee821f56793c2e8/image.png)

정보 수정 버튼을 클릭해면, 지금 자신(맴버/클럽)의 기본 정보가 입력되어있는 창이 뜨며, 여기의 값을 바꿔 정보를 수정 할 수 있다.





=======================================================================

![image](/uploads/d174086e6c0a840f28cba59b04999913/image.png)

![image](/uploads/fdabc87278de3c8e60039bfa390b6a33/image.png)

맴버쉽 탈퇴 버튼을 누르면, 현재 맴버가 가입한 클럽 또는, 현재 클럽에 가입된 맴버쉽을 확인 할 수있으며, 맴버쉽 ID를 입력하여 맴버쉽을 탈퇴하거나 탈퇴 시킬 수 있다.



-- 나머지 시연 기능 사진은 생략.