subarch: rv64_lp64d
target: stage3
version_stamp: @TIMESTAMP@
cflags: -O2 -pipe
interpreter: /usr/bin/qemu-riscv64
rel_type: default
profile: default/linux/riscv/17.0/rv64gc/lp64d
snapshot: @TIMESTAMP@
source_subpath: default/stage2-rv64_lp64d-@TIMESTAMP@
compression_mode: pixz
decompressor_search_order: xz bzip2
portage_confdir: @REPO_DIR@/releases/portage/stages-qemu
portage_prefix: releng
