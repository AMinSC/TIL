# 사전 CS와 네트워크

## HW와 SW 관련 간단한 용어 정리

### 하드웨어 (HW):

1. **CPU (Central Processing Unit: 중앙 처리 장치)**: "컴퓨터의 뇌"라고도 불립니다. 소프트웨어의 지시사항을 실행합니다.

2. **RAM (Random Access Memory: 랜덤 액세스 메모리)**: 현재 사용하거나 처리 중인 데이터를 저장하는 임시 메모리입니다.

3. **HDD (Hard Disk Drive: 하드 디스크 드라이브) & SSD (Solid State Drive: 솔리드 스테이트 드라이브)**: 영구 저장 장치입니다. SSD는 HDD보다 빠르지만 비용이 더 많이 듭니다.

4. **Motherboard(메인보드)**: CPU, RAM 및 기타 필수 구성 요소가 장착된 주요 회로 기판입니다.

5. **GPU (Graphics Processing Unit: 그래픽 처리 장치)**: 이미지와 비디오의 렌더링을 처리합니다. 게임 및 그래픽 디자인과 같은 작업에 특히 중요합니다.

6. **I/O Ports (Input/Output Ports: 입력/출력 포트)**: USB 포트와 같은 컴퓨터에 외부 장치를 연결하는 슬롯입니다.

7. **Power Supply(전원 공급기)**: 전원 공급 장치는 콘센트로부터 전기를 컴퓨터 구성 요소가 사용할 수 있는 형태로 변환합니다.

8. **Peripheral Devices(주변 장치)**: 키보드, 마우스 및 프린터와 같이 컴퓨터에 연결하는 외부 장치입니다.


### 소프트웨어 (SW):

1. **OS (Operating System: 운영 체제)**: 하드웨어를 관리하고 다른 소프트웨어에 대한 서비스를 제공하는 기본 소프트웨어입니다. 예: Windows, macOS, Linux.

2. **Application Software(응용 프로그램 소프트웨어)**: 사용자가 특정 작업을 수행할 수 있게 해주는 프로그램입니다. 예: Microsoft Word, Photoshop, 웹 브라우저.

3. **Drivers(드라이버)**: OS가 하드웨어 장치와 통신할 수 있게 해주는 소프트웨어입니다.

4. **Firmware(펌웨어)**: 하드웨어 장치에 내장된 특별한 소프트웨어로, 그 장치가 어떻게 동작해야 하는지의 지침을 제공합니다.

5. **Middleware(미들웨어)**: 운영 체제와 응용 프로그램 사이에서 다리 역할을 하는 소프트웨어입니다.

6. **Utilities(유틸리티)**: 시스템의 관리나 유지보수와 관련된 특정한 작업을 위한 작은 프로그램들입니다. 예: 디스크 청소 도구, 바이러스 백신.

7. **API (Application Programming Interface: 응용 프로그래밍 인터페이스)**: 서로 다른 소프트웨어 애플리케이션이 서로 통신할 수 있게 해주는 규칙과 도구들입니다.

8. **IDE (Integrated Development Environment: 통합 개발 환경)**: 개발자가 코드를 작성, 테스트, 디버그하는데 사용되는 소프트웨어입니다. 예: Visual Studio, Eclipse.


---
## OSI 7 계층에 대한 기초

### OSI (Open Systems Interconnection) 모델
네트워크 상호 작용을 이해하기 위한 개념적 프레임워크로 일곱 개의 독립적인 계층으로 구성되어 있습니다. 각 계층은 특정한 기능을 갖고 있으며 직접적으로는 바로 위나 아래의 계층하고만 상호 작용합니다.

### 1. Physical Layer: 물리 계층 (계층 1)
- **목적**: 장치 간의 물리적 연결에 관련되어 있습니다.
- **기능**: 전기 또는 광 신호와 같은 물리적 매체를 통한 원시 비트의 전송 및 수신과 관련되어 있습니다.
- **예시**: 케이블 (이더넷, 동축 케이블), 스위치, 허브, 리피터.

### 2. DataLink Layer: 데이터 링크 계층 (계층 2)
- **목적**: 물리 계층을 통한 오류 없는 전송을 보장합니다.
- **기능**: 출력 데이터를 프레임으로 나누고 물리 계층에서의 오류를 처리합니다. MAC 주소가 이곳에 있습니다.
- **예시**: 브리지, 스위치, NIC (네트워크 인터페이스 카드), MAC 주소.

### 3. Network Layer: 네트워크 계층 (계층 3)
- **목적**: 네트워크 간 데이터 전송의 최적의 경로를 결정합니다.
- **기능**: 패킷 포워딩, 라우팅 및 주소 지정과 관련됩니다. IP 주소가 이곳에 있습니다.
- **예시**: 라우터, IP 주소, IPX, AppleTalk.

### 4. Transport Layer: 전송 계층 (계층 4)
- **목적**: 종단 간 통신, 데이터 무결성 및 오류 수정을 보장합니다.
- **기능**: 오류 검사 및 데이터 세그먼테이션을 제공합니다. 얼마나 많은 데이터를 한 번에 보낼지 결정합니다. 포트가 이곳에 있습니다.
- **예시**: TCP, UDP, 포트.

### 5. Session Layer: 세션 계층 (계층 5)
- **목적**: 응용 프로그램 간의 연결을 설정, 유지 및 종료합니다.
- **기능**: 대화 제어를 사용하여 세션을 관리합니다 (데이터 동기화 유지).
- **예시**: RPC (원격 프로시저 호출), PPTP (포인트 투 포인트 터널링 프로토콜).

### 6. Presentation Layer: 표현 계층 (계층 6)
- **목적**: 응용 프로그램과 전송 계층 간의 데이터 변환을 합니다.
- **기능**: 데이터 형식 변환, 암호화 및 압축을 제공합니다.
- **예시**: SSL/TLS, JPEG, GIF, MPEG.

### 7. Application Layer: 응용 계층 (계층 7)
- **목적**: 응용 프로세스에 네트워크 서비스를 제공합니다.
- **기능**: 다른 계층이 효과적으로 활용되도록 합니다. 네트워크 상에서 소프트웨어 애플리케이션이 통신하기 위해 사용하는 프로토콜이 포함됩니다.
- **예시**: HTTP, FTP, SMTP, POP3, SNMP.

실제 네트워킹에서는 이 일곱 계층 모델이 완벽하게 적용되지 않을 수 있습니다. OSI 모델은 이론적이기 때문에, 실제로는 4개 계층으로 구성된 TCP/IP 모델이 더 일반적으로 사용되는 모델입니다.

---
## 위에서 다룬 각 영역별로 보안과 관련된 요소들을 알아보겠습니다. 

### 1. **HW (Hardware :하드웨어)**
- **HSMs (Secure Hardware Modules: 보안 하드웨어 모듈)**: 강력한 인증을 위한 디지털 키를 보호하고 관리하는 물리적 장치이며 암호 처리를 제공합니다.
- **TPM (Trusted Platform Module: 신뢰 플랫폼 모듈)**: 컴퓨터의 보안을 강화하는 안전한 암호 프로세서입니다.
- **Hardware-based Firewalls: 하드웨어 기반 방화벽**: 네트워크 간의 장벽을 제공하여 보안 정책을 기반으로 트래픽을 허용하거나 거부합니다.

### 2. **SW (Software: 소프트웨어)**
- **Antivirus & Antimalware Software: 안티바이러스 및 안티맬웨어 소프트웨어**: 악성 소프트웨어를 감지, 예방 및 제거하는 프로그램입니다.
- **Firewall Software: 방화면 소프트웨어**: 들어오고 나가는 네트워크 트래픽을 모니터링하고 제어합니다.
- **Encryption Software: 암호화 소프트웨어**: 데이터를 보호하기 위해 암호화 기법을 사용하는 도구입니다.
- **IDPS (Intrusion Detection & Prevention Systems: 침입 탐지 및 예방 시스템)**: 네트워크나 시스템에서 악성 활동을 모니터링하는 소프트웨어입니다.

### 3. **OSI 7 Layer Model**
While security can be implemented at multiple layers of the OSI model, certain layers are more commonly associated with specific security measures:

- **Physical Layer**: Physical security measures like securing cables or using tamper-evident seals.
- **Data Link Layer**: MAC address filtering and switch port security.
- **Network Layer**: Packet filtering with the help of Access Control Lists (ACLs) on routers. IPsec can also be used here for encrypting IP packets.
- **Transport Layer**: Security measures such as Secure Sockets Layer (SSL) and Transport Layer Security (TLS) for encrypting sessions.
- **Session Layer**: VPN tunnels can be established at this layer to create a secure connection over a public network.
- **Presentation Layer**: Encryption, compression, and translating data between formats can occur here, with SSL/TLS operating at both this layer and the transport layer.
- **Application Layer**: Firewalls can filter traffic based on the application. Protocols like HTTPS (HTTP over SSL/TLS) also work at this layer.

It's essential to understand that security is a layered approach. The more layers at which security is implemented, the harder it is for malicious entities to penetrate or compromise a system or network. Combining HW, SW, and OSI layer-specific security measures can result in a robust and comprehensive security posture.

