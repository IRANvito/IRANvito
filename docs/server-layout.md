# Server layout (file locations)

Everything lives in a tidy, predictable layout. You can also see this any time
from **Manage → File Locations** in the CLI.

| Path | What |
|------|------|
| `/root/IRANvito` | The release bundle and downloaded archives. |
| `/root/IRANvito/backups` | [Backup](backup-restore.md) `.tar.gz` files. |
| `/etc/iranvito` | Tunnel configs (one `.toml` per tunnel) and runtime state. |
| `/usr/local/bin/iranvito` | The binary itself. |
| `iranvito-<name>.service` | A systemd unit per tunnel. |
| `iranvito-monitor.service` | The [monitor service](monitor-service.md). |

The install directory is recorded in `/etc/iranvito/install_path`, which is what
the uninstaller reads to know what to remove.

---

<div dir="rtl">

## خلاصهٔ فارسی

همه‌چیز در یک ساختار مرتب و قابل‌پیش‌بینی است. همین را هر وقت خواستی از
`Manage → File Locations` در CLI هم می‌بینی.

`‎/root/IRANvito` بستهٔ ریلیز و آرشیوهای دانلودشده ·
`‎/root/IRANvito/backups` فایل‌های [پشتیبان](backup-restore.md) ·
`‎/etc/iranvito` کانفیگ تونل‌ها (برای هر تونل یک فایل `.toml`) و وضعیت اجرا ·
`‎/usr/local/bin/iranvito` خودِ باینری ·
`iranvito-<name>.service` یک یونیت systemd به‌ازای هر تونل ·
`iranvito-monitor.service` [سرویس مانیتور](monitor-service.md).

مسیر نصب در `/etc/iranvito/install_path` ثبت می‌شود و حذف‌کنندهٔ داخلی از روی
همان می‌فهمد چه چیزی را پاک کند.

</div>

---
[← Back to the docs index](README.md)

---

*Last verified against IRANvito v2.0.0.*
