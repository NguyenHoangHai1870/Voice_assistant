# Voice Assistant AI

AI Voice Assistant chạy local, hỗ trợ giao tiếp bằng giọng nói/text, quản lý lịch, điều khiển tác vụ cơ bản và trả lời thông tin bằng FAQ + Local LLM.

---

# 1. Công nghệ sử dụng

- Python 3.11
- FastAPI
- WebSocket
- PostgreSQL
- Docker / Docker Compose
- Ollama (Local LLM)
- SentenceTransformers (Semantic FAQ Retrieval)
- Scikit-learn (Intent Classification)

---

# 2. Chức năng chính

## Speech To Text
- Nhận audio `.m4a` qua WebSocket
- Chuyển giọng nói thành văn bản

## Intent Classification
- Phân loại ý định người dùng:
  - calendar
  - control_device
  - qa

## Calendar Management
- Thêm lịch
- Xóa lịch
- Kiểm tra lịch

## Device Control
- Mở website / search / youtube / app local

## FAQ Semantic Retrieval
- Trả lời nhanh các câu hỏi phổ biến bằng embedding retrieval

## Personalization / Memory
- Ghi nhớ sở thích / thông tin người dùng

## LLM Fallback
- Nếu không match FAQ → fallback sang Local LLM

---

# 3. Cấu trúc thư mục

```bash
voice-assistant/
│
├── app/
│   ├── main.py
│   ├── orchestrator.py
│   ├── services/
│   └── config/
│   
│
├── data/
│   ├── data_R.csv
│   └── faq_knowledge.json
│
├── models/
│   ├── intent_model.pkl
│   ├── faq_embeddings.npy
│   └── faq_index_map.json
│
├── Dockerfile
├── docker-compose.yml
├── init.sql
├── requirements.txt
├── .env.example
└── README.md


4. Yêu cầu trước khi chạy

Cần cài đặt:

Docker Desktop
Python 3.11+
Ollama

5. Clone project
git clone <repo_url>
cd voice-assistant

6. Tạo file môi trường

Copy file mẫu:

copy .env.example .env

7. Nội dung .env
POSTGRES_HOST=db
POSTGRES_PORT=5433
POSTGRES_DB=assistant_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=123456

OLLAMA_URL=http://host.docker.internal:11434

8. Khởi động hệ thống bằng Docker
docker-compose up --build

Docker sẽ tự động:

Build FastAPI app
Start PostgreSQL
Init database bằng init.sql

9. Cài Ollama và Model
Start Ollama
ollama serve
Pull model
ollama pull qwen2.5:1.5b

10. Train Intent Model

Sau khi chỉnh dataset:

python app/train_intent.py

Output:

models/intent_model.pkl

11. Build FAQ Embeddings

Sau khi chỉnh FAQ knowledge:

python app/build_faq_embeddings.py

Output:

models/faq_embeddings.npy
models/faq_index_map.json

12. Chạy Server Local (Không Docker)
uvicorn app.main:app --reload

13. WebSocket Endpoint
ws://localhost:8000/ws

14. Test WebSocket Audio

test chat: test_chat.py
test audio: wstest.py

15. Database Schema

Database gồm các bảng:

users
reminders
user_profiles
user_hobbies
conversation_memory
user_behaviors

Schema được khởi tạo tự động từ:

init.sql

16. Workflow xử lý request
Audio/Text Input
      ↓
Speech To Text (nếu audio)
      ↓
Intent Classification
      ↓
Route Service
 ├── Calendar Handler
 ├── Device Control
 └── QA Router
        ↓
 FAQ Retrieval / Memory / LLM

17. Một số ví dụ câu lệnh hỗ trợ
Calendar
Nhắc tôi họp lúc 8 giờ sáng
Hôm nay tôi có lịch gì
Hủy lịch ngày mai lúc 6h
Device Control
Mở youtube
Mở nhạc trẻ trên youtube
Tìm blockchain là gì
QA
Machine learning là gì
Hôm nay thời tiết thế nào

18. Lưu ý
Với audio:
Hỗ trợ .m4a
STT tốc độ phụ thuộc model local
Với device control:
Một số chức năng chỉ hoạt động local trên máy host

19. Thành viên clone project cần làm gì
copy .env.example .env
docker-compose up --build
ollama serve
ollama pull qwen2.5:3b

Sau đó project sẵn sàng tại:

ws://localhost:8000/ws
20. Troubleshooting
Missing intent_model.pkl
python app/train_intent.py
Missing FAQ embeddings
python app/build_faq_embeddings.py
Cannot connect to Ollama

Kiểm tra:

ollama serve

