# GUI 자습 (WEEK2 주말과제)

## 07/19

### GUI의 정의
* 목적
    - 사용자와 상호작용을 원활히 하기 위해서
    - 그래픽 사용자 인터페이스를 의미함
    - 현대적인 프로그램은 대부분 그래픽 사용자 인터페이스(gui)를 제공하여 정보를 표시
    - 명령줄 프로그램과 달리 gui애플리케이션은 대개 이벤트 주도이다. 즉 키 입력과 마우스 클릭 같은 이벤트가 일어날때마다 반응
    - 경험상 GUI는 모델-뷰-컨트롤러 패턴으로 만들어야 한다. 모델은 조잘할 데이터고, 뷰는 데이터의 현재 상태를 표시하고 사용자 입력을 가져오며, 컨트롤러는 다음에 무엇을 할지 결정
    
* 사용 모듈
    - __tkinter__ 
    - python에서 제공하는 기본 GUI
    - [DOCS](https://docs.python.org/ko/3/library/tkinter.html)   
    - 간단한 프로그램
    <pre>
    <code>
    import tkinter
    window = tkinter.TK()
    window.mainloop()
    </pre>
    </code>

* __tkinter 위젯__
1. 라벨(Label)
    - 설명 : 짧은 한 줄 짜리 텍스트 표시
    - __pack()__ : 위젯마다 들어 있는 pack메서드는 부모 위젯에 자신을 넣고 부모에게 필요에 따라 크기를 조정하라고 알려줌
        - 매개변수 side를 통해 LEFT,RIGHT,TOP,BOTTOM으로 각 객체를 배치할 수 있다.
    - __grid()__ : 윈도우를 각 표로 나누어 각 표의 위치에 맞게 놓는 방법
        - 매개변수 row, column, rowspan, columnsapn 활용 가능
    - __place()__ : 윈도우에 절대 위치로 각 위젯을 배치하는 구조
    - __config()__ 메서드 : 간단히 위젯의 텍스트에 새로운 값을 할당할 수 있다.
    - 컨테이너의 값은 __set__ 과 __get__ 메서드로 할당하고, 추출
***
2. 프레임(Frame)
    - 구역화


3. Button
    - Button은 클릭으로 다양한 이벤트를 연결할 수 있는 GUI
    - ```w = Button(master, option=value,....)```
    <pre>
    <code>
    from tkinter

    window = tkinter.Tk()
    b1 = Button(window, width =10, height=10, text = "say hello")
    b1.pack()
    window.mainloop()
    </pre>
    </come>

4. Checkbutton
    - *체크박스* 라고도 불리며, 체크버튼에는 on과 off 두가지 상태가 있다.  
    - 일반적으로 IntVal 변수를 사용하고, 값 1과 0이 각각 온과 오프를 가리킨다.

5. Entry
    - 한줄로 표현해야한느 부분에 대해서 입력 받거나 할 경우에 사용하는 부분
    - ```w= Entry(target, option....)```
    - target : 체크버튼을 표시할 타겟
    - option : 체크버튼에 대한 세부 설정

### GUI와 모델, 뷰, 컨트롤러
<pre>
1. 모델: 데이터를 어떻게 표현하는 것
    -> 애플리케이션의 현재 상태를 기록
2. 뷰 : 데이터를 어떻게 표시하는가
    -> Label, entry
3. 컨트롤러 : 데이터를 어떻게 수정하는가
            : 사용자 입력을 데이터를 조작하는 모델 내 함수로 변환 
</pre>

- MVC디자인은 애플리케이션을 쉽게 이해하고 수정할 수 있도록 애플리케이션 부분 부분을 나누는 것
- 이를 통해 데이터를 조작하는 코드에 영향을 주지 않으면서 GUI코드를 변경하기 쉬워진다.
 