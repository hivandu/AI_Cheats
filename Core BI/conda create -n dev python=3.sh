conda create -n dev python=3.11
conda activate dev
conda install mlx mlx-lm mlx-vlm
pip install torch torchvision torchaudio
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-2.8.0+cpu.html
pip install torch_geometric
conda install xgboost lightgbm ngboost opencv matplotlib jupyterlab notebook seaborn scikit-learn scikit-image
conda install nltk jieba wordcloud flask dash pydotplus StatsForecast pyecharts Ultralytics Cython pandas-datareader implicit yfinance pygame
conda install node2vec lightfm catboost # numpy==1.26
