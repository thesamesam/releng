subarch: s390
version_stamp: @TIMESTAMP@
target: stage3
rel_type: default
profile: default/linux/s390/17.0
snapshot: @TIMESTAMP@
source_subpath: default/stage1-s390-@TIMESTAMP@
compression_mode: pixz_x
decompressor_search_order: tar pixz xz lbzip2 bzip2 gzip
portage_confdir: @REPO_DIR@/releases/portage/stages
pkgcache_path: /var/tmp/catalyst/packages/default/stage3-s390