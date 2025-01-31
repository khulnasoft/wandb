# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wandb/proto/wandb_settings.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n wandb/proto/wandb_settings.proto\x12\x0ewandb_internal\x1a\x1egoogle/protobuf/wrappers.proto\" \n\x0fListStringValue\x12\r\n\x05value\x18\x01 \x03(\t\"\x1d\n\x0cListIntValue\x12\r\n\x05value\x18\x01 \x03(\x05\"\x8a\x01\n\x17MapStringKeyStringValue\x12\x41\n\x05value\x18\x01 \x03(\x0b\x32\x32.wandb_internal.MapStringKeyStringValue.ValueEntry\x1a,\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xcb\x01\n#MapStringKeyMapStringKeyStringValue\x12M\n\x05value\x18\x01 \x03(\x0b\x32>.wandb_internal.MapStringKeyMapStringKeyStringValue.ValueEntry\x1aU\n\nValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue:\x02\x38\x01\"\x9a\x01\n\x12OpenMetricsFilters\x12\x33\n\x08sequence\x18\x01 \x01(\x0b\x32\x1f.wandb_internal.ListStringValueH\x00\x12\x46\n\x07mapping\x18\x02 \x01(\x0b\x32\x33.wandb_internal.MapStringKeyMapStringKeyStringValueH\x00\x42\x07\n\x05value\"7\n\tRunMoment\x12\x0b\n\x03run\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x0e\n\x06metric\x18\x03 \x01(\t\"\xcfJ\n\x08Settings\x12-\n\x07\x61pi_key\x18\x37 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x13identity_token_file\x18\xaa\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x10\x63redentials_file\x18\xab\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x14insecure_disable_ssl\x18\xb9\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08_offline\x18\x1e \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06x_sync\x18\x1f \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\tsync_file\x18\x86\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x07_shared\x18\xa2\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x06run_id\x18k \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07run_url\x18q \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07project\x18\x61 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x65ntity\x18\x45 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cx_start_time\x18) \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12.\n\x08root_dir\x18i \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07log_dir\x18U \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0clog_internal\x18V \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tfiles_dir\x18\x46 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0bx_files_dir\x18\xb4\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0cignore_globs\x18N \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12.\n\x08\x62\x61se_url\x18\x39 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\x17x_file_stream_max_bytes\x18\xac\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x46\n\x1fx_file_stream_transmit_interval\x18\xaf\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x45\n\x14x_extra_http_headers\x18\x0e \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12=\n\x17x_file_stream_retry_max\x18\x93\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12K\n$x_file_stream_retry_wait_min_seconds\x18\x94\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12K\n$x_file_stream_retry_wait_max_seconds\x18\x95\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x43\n\x1dx_file_stream_timeout_seconds\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x42\n\x1cx_file_stream_max_line_bytes\x18\xb2\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12?\n\x19x_file_transfer_retry_max\x18\x96\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12M\n&x_file_transfer_retry_wait_min_seconds\x18\x97\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12M\n&x_file_transfer_retry_wait_max_seconds\x18\x98\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x46\n\x1fx_file_transfer_timeout_seconds\x18\x99\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x39\n\x13x_graphql_retry_max\x18\x9a\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12G\n x_graphql_retry_wait_min_seconds\x18\x9b\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12G\n x_graphql_retry_wait_max_seconds\x18\x9c\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12@\n\x19x_graphql_timeout_seconds\x18\x9d\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x31\n\nhttp_proxy\x18\xa8\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0bhttps_proxy\x18\xa9\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\tx_proxies\x18\xc8\x01 \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12-\n\x07program\x18_ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fprogram_relpath\x18` \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x10_code_path_local\x18\xa3\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x0fprogram_abspath\x18\x9f\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x05_args\x18\x01 \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12)\n\x03_os\x18  \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x64ocker\x18\x43 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0cx_executable\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07_python\x18\" \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\tcolab_url\x18\xa0\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04host\x18M \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x08username\x18\x8d\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x05\x65mail\x18\x44 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06resume\x18\x66 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0bresume_from\x18\xa7\x01 \x01(\x0b\x32\x19.wandb_internal.RunMoment\x12-\n\tfork_from\x18\xa4\x01 \x01(\x0b\x32\x19.wandb_internal.RunMoment\x12\x38\n\x14\x64isable_job_creation\x18\x41 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\tsweep_url\x18\x83\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x16x_disable_update_check\x18\xa5\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0ex_disable_meta\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\tsave_code\x18s \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x0b\x64isable_git\x18? \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x16x_disable_machine_info\x18\x9e\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0fx_disable_stats\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x13x_stats_buffer_size\x18\xa1\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12@\n\x19x_stats_sampling_interval\x18\xae\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x30\n\x0bx_stats_pid\x18* \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12<\n\x12x_stats_disk_paths\x18\x92\x01 \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12H\n\"x_stats_neuron_monitor_config_path\x18. \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\x15x_stats_dcgm_exporter\x18\xbb\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12O\n\x1ex_stats_open_metrics_endpoints\x18/ \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12H\n\x1cx_stats_open_metrics_filters\x18\x30 \x01(\x0b\x32\".wandb_internal.OpenMetricsFilters\x12S\n!x_stats_open_metrics_http_headers\x18\xb8\x01 \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12=\n\x16x_stats_gpu_device_ids\x18\xba\x01 \x01(\x0b\x32\x1c.wandb_internal.ListIntValue\x12.\n\x07x_label\x18\xb5\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12=\n\x18x_require_legacy_service\x18\xad\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x16x_show_operation_stats\x18\xb0\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\tx_primary\x18\xb6\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x15x_update_finish_state\x18\xb7\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12<\n\x17\x61llow_offline_artifacts\x18\xb1\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\x07\x63onsole\x18< \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x11\x63onsole_multipart\x18\xa6\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x10sync_tensorboard\x18\xb3\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x0b_aws_lambda\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0fx_cli_only_mode\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06_colab\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x11x_disable_service\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12:\n\x16x_disable_setproctitle\x18\t \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x10x_disable_viewer\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x15x_flow_control_custom\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12;\n\x17x_flow_control_disabled\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12>\n\x18x_internal_check_process\x18\x12 \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12,\n\x08_ipython\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08_jupyter\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x0ex_jupyter_root\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x07_kaggle\x18\x17 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12=\n\x18x_live_policy_rate_limit\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12<\n\x17x_live_policy_wait_time\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x0bx_log_level\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x10x_network_buffer\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12)\n\x05_noop\x18\x1c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\t_notebook\x18\x1d \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\t_platform\x18! \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12x_runqueue_item_id\x18# \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x13x_save_requirements\x18% \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x39\n\x13x_service_transport\x18& \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0ex_service_wait\x18\' \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12\x35\n\x0f_start_datetime\x18( \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\r_tmp_code_dir\x18\x31 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x08_windows\x18\x34 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x34\n\x10\x61llow_val_change\x18\x35 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\tanonymous\x18\x36 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12P\n\x1f\x61zure_account_url_to_access_key\x18\x38 \x01(\x0b\x32\'.wandb_internal.MapStringKeyStringValue\x12.\n\x08\x63ode_dir\x18: \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0c\x63onfig_paths\x18; \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12\x30\n\ndeployment\x18= \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0c\x64isable_code\x18> \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\rdisable_hints\x18@ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12,\n\x08\x64isabled\x18\x42 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12)\n\x05\x66orce\x18G \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\ngit_commit\x18H \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\ngit_remote\x18I \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0egit_remote_url\x18J \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08git_root\x18K \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x11heartbeat_seconds\x18L \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x32\n\x0cinit_timeout\x18O \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12,\n\x08is_local\x18P \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x30\n\njob_source\x18Q \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\rlabel_disable\x18R \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06launch\x18S \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x38\n\x12launch_config_path\x18T \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14log_symlink_internal\x18W \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10log_symlink_user\x18X \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08log_user\x18Y \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rlogin_timeout\x18Z \x01(\x0b\x32\x1c.google.protobuf.DoubleValue\x12*\n\x04mode\x18\\ \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rnotebook_name\x18] \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bproject_url\x18\x62 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12)\n\x05quiet\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06reinit\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x07relogin\x18\x65 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0cresume_fname\x18g \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12+\n\x07resumed\x18h \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\trun_group\x18j \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0crun_job_type\x18l \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08run_mode\x18m \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08run_name\x18n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\trun_notes\x18o \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x08run_tags\x18p \x01(\x0b\x32\x1f.wandb_internal.ListStringValue\x12\x35\n\x11sagemaker_disable\x18r \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x35\n\x0fsettings_system\x18t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12settings_workspace\x18u \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0bshow_colors\x18v \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12.\n\nshow_emoji\x18w \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x0bshow_errors\x18x \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\tshow_info\x18y \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x31\n\rshow_warnings\x18z \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12*\n\x06silent\x18{ \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0cstart_method\x18| \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x06strict\x18} \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0esummary_errors\x18~ \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x34\n\x0fsummary_timeout\x18\x7f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x36\n\x10summary_warnings\x18\x80\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\x08sweep_id\x18\x81\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x10sweep_param_path\x18\x82\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x07symlink\x18\x84\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x08sync_dir\x18\x85\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x13sync_symlink_latest\x18\x87\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12J\n%table_raise_on_max_row_limit_exceeded\x18\x8a\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12/\n\x08timespec\x18\x8b\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x07tmp_dir\x18\x8c\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\twandb_dir\x18\x8e\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0ex_jupyter_name\x18\x8f\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0ex_jupyter_path\x18\x90\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x08job_name\x18\x91\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueJ\x04\x08\x03\x10\x04J\x04\x08\x06\x10\x07J\x04\x08\x0c\x10\rJ\x04\x08\x13\x10\x14J\x04\x08$\x10%J\x04\x08+\x10,J\x04\x08,\x10-J\x04\x08-\x10.J\x04\x08\x32\x10\x33J\x04\x08\x33\x10\x34J\x04\x08[\x10\\J\x04\x08^\x10_J\x06\x08\x88\x01\x10\x89\x01J\x06\x08\x89\x01\x10\x8a\x01\x42\x1bZ\x19\x63ore/pkg/service_go_protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wandb.proto.wandb_settings_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\031core/pkg/service_go_proto'
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._options = None
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_options = b'8\001'
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._options = None
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_options = b'8\001'
  _LISTSTRINGVALUE._serialized_start=84
  _LISTSTRINGVALUE._serialized_end=116
  _LISTINTVALUE._serialized_start=118
  _LISTINTVALUE._serialized_end=147
  _MAPSTRINGKEYSTRINGVALUE._serialized_start=150
  _MAPSTRINGKEYSTRINGVALUE._serialized_end=288
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_start=244
  _MAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_end=288
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE._serialized_start=291
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE._serialized_end=494
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_start=409
  _MAPSTRINGKEYMAPSTRINGKEYSTRINGVALUE_VALUEENTRY._serialized_end=494
  _OPENMETRICSFILTERS._serialized_start=497
  _OPENMETRICSFILTERS._serialized_end=651
  _RUNMOMENT._serialized_start=653
  _RUNMOMENT._serialized_end=708
  _SETTINGS._serialized_start=711
  _SETTINGS._serialized_end=10262
# @@protoc_insertion_point(module_scope)
