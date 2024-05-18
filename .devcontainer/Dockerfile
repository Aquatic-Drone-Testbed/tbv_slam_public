FROM ros:noetic-perception

ARG USERNAME=tbv-seamate-docker
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install build dependencies
RUN apt-get clean && \
    # apt-get update && \
    apt-get install -y wget software-properties-common python3-catkin-tools libgoogle-glog-dev libgflags-dev libatlas-base-dev libeigen3-dev libsuitesparse-dev libfmt-dev psmisc ros-noetic-tf-conversions libboost-all-dev python3-pybind11 libzip-dev python3-pip libspdlog-dev ros-noetic-rviz && \
    rm -rf /var/lib/apt/lists/

RUN wget ceres-solver.org/ceres-solver-2.1.0.tar.gz
RUN tar zxf ceres-solver-2.1.0.tar.gz
RUN mkdir ceres-bin
WORKDIR /ceres-bin
RUN cmake ../ceres-solver-2.1.0
# change the following line to -jx which x is a number for multi threading to parallel compile from source. 
# default is: -j8
RUN make -j4
RUN make install

RUN pip3 install numpy --upgrade
RUN pip3 install scikit-learn seaborn tqdm tabulate

USER $USERNAME

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc

WORKDIR /home/ws