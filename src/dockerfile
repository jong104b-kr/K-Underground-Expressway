FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN python -m py_compile src/model/*.py   # 간단한 컴파일 검증

# 모델 가중치 복사 (빌드 시 미리 넣어 두면 좋음)
# COPY model_weights.pth /app/model_weights.pth

CMD ["python", "-m", "my_awesome_repo.train.trainer"]
