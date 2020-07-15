# 도커에서 이미지 설치
Docker pull (이미지)
# 실행중인 docker container 확인
Docker ps
# 실행중인 것과 stop 된 container 확인
Docker ps –a (-all)
# container stop
Docker strop (name)
# stop 된 컨테이너 다시 시작
Docker start (name)
# container 이름변경
Docker rename container-name container-rename
Ex) docker rename webserver web
Docker ps
# Ubuntu, centos:7 image download
Docker pull Ubuntu
Docker pull centos:7  # centos:version(tag)

# image 상세보기 – image config dockerfile 조회
Docker image inspect (image-name)
# prune은 사용하지 않는 image들을 한꺼번에 삭제한다.
# 이미지를 특정해서 삭제하려면 rm으로 사용.
# 이미지를 사용하는 container가 있다면, 이미지가 삭제 안된다.
# Exit 해도 컨테이너가 있다면 컨테이너부터 지워야 한다.
Docker container(<-생략가능) rm (container_name)

# image 삭제 – image를 사용하는 container가 있을 경우, 사용하는 container 부터 삭제 후 삭제.
Docker image rm (image_name of image_ID)

# ubuntu, centos:7 container 생성/실행(create/start)
# centos의 /bin/cal – calender 실행 –it:표준입출력 사용
docker run -it --name centos_cal centos:7 /bin/cal
docker ps –a
docker run –it –name centos_shell centos:7 /bin/bash
111 111 111
(7   7   7 : 모든 권한이 모두에게 개방)
111 101 101 : -rwxr-xr-x
(7   5   5 : admin 은 읽고, 쓰고, 실행 가능. 나머지는 쓰기는 불가능)
수정 하려면 chmod 755 처럼 수정 가능
# exit된 container를 다시 시작
Docker start –I (container_name)
이 상태에서 ctrl + p + q 를 하면 container가 up되어 있는 상태에서 도커로 돌아오게 됨.
이후 다시 container로 돌아가려면
Docker attach (container_name)
root@:/#
![image](/uploads/3fc8386fda87dfbceef64557cd11a880/image.png)


--------------------------------------------------------------------------------------
#docker image 검색
#docker search image명
docker search nginx

#docker image download
#docker pull image명
docker pull nginx

#docker image list
#docker images  또는 docker image ls
docker images

#conatiner 실행
#docker container run --name conatiner-name -d -p port:port image명
#-d :detach(background로 실행), -p:publish(포트 포워딩)
docker container run --name webserver -d -p 80:80 nginx

#실행중인 container 확인
docker ps

#실행중이거나 실행했던 constainer 확인
docker ps -a

#Exited된 container 삭제
#docker rm container-name
docker rm hellworld
docker ps -a

#container 이름변경
#docker rename container-name container-rename
docker reanme webserver web
docker ps -a

#container 중지
#docker stop container-name
docker stop web

#container 실행
docker start web

#ubuntu, centos:7  image download
docker pull ubuntu
docker pull centos:7 #centos:version(tag)
docker images

#image 상세보기 - image config .Dockerfile 조회
docker image inspect ubuntu

#image 삭제 - image사용하는 container가 있을 경우 사용하는 container 삭제 후 삭제
docker image rm imageID

#사용하지 않는 image삭제
docker image prune

#ubuntu, centos:7 conatiner 생성/실행(create/start)
#centos의 /bin/cal - calendar 실행 -it:표준입출력 사용
docker run -it --name centos_cal centos:7 /bin/cal
docker ps -a
docker run -it --name centos_shell centos:7 /bin/bash //centos:7 bash명령실행
root@:/#adduser test1  //test1 user 생성
root@:/#su test        //test1 user로 변경
test@:/$ ls -al         //목록보기          
test@:/$ exit           //root로 가기
root@:/# exit           //docker 로 가기

docker ps -a            //centos_shell은 exited 상태

root@:/#      //ctrl+p+q docker 로 가기
docker ps -a            //centos_shell은 Up 상태
docker attach centos_shell  //root로
root@:/#cat /etc/issue  //centos 버전확인
root@:/#ctrl+p+q


#ubuntu 실행 확인
docker run -it --name ubuntu_shell ubuntu /bin/bash
root@:/#cat /etc/issue  //ubuntu 버전확인 - centos와 비교
root@:/#adduser user1  //user생성
root@:/#passwd root  //root계정 암호설정
root@:/#
root@:/# ctrl+p+q


docker ps  //web,ubuntu_shell, centos_shell 실행 중
docker ps -q //실행중인 container id만 출력
docker stop `docker ps -q` //실행중인 id 모두 stop
docker start `docker ps -a -q` //모든 container start
docker ps
for index in `docker ps -q`;do echo $index; done //실행중인 container id list
for index in `docker ps -q`;do echo $index; docker stop $index;done //실행중인 id 모두 stop
