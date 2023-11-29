

str1 = """
#
#-------------------------------------------------------------#
#  创建时间：2023-10-25 23:49:10
#-------------------------------------------------------------#
#
mixed-port: 7890
allow-lan: true
mode: Rule
log-level: info
external-controller: 0.0.0.0:9090
dns:
  enabled: true
  nameserver:
    - 119.29.29.29
    - 223.5.5.5
  fallback:
    - 8.8.8.8
    - 8.8.4.4
    - tls://1.0.0.1:853
    - tls://dns.google:853
proxies:
  #- {"type":"vless","name":"HKG","server":"162.159.134.216","port":80,"uuid":"6386b476-d9b1-4ec8-953c-d682a22a01f7","skip-cert-verify":true,"udp":false,"tls":false,"network":"ws","servername":"hello.patvice.workers.dev","ws-opts":{"path":"/?ed=2048","headers":{"host":"hello.patvice.workers.dev"}}}
  #- {"type":"vless","name":"SJP","server":"104.17.212.213","port":80,"uuid":"6386b476-d9b1-4ec8-953c-d682a22a01f7","skip-cert-verify":true,"udp":false,"tls":false,"network":"ws","servername":"hello.patvice.workers.dev","ws-opts":{"path":"/?ed=2048","headers":{"host":"hello.patvice.workers.dev"}}}
"""


proxy1 = """
proxy-groups:
  - name: 🚀 节点选择
    type: select
    proxies:
      - ♻️ 自动选择
      - DIRECT
"""

proxy2 = """
  - name: ♻️ 自动选择
    type: url-test
    url: http://www.gstatic.com/generate_204
    interval: 300
    tolerance: 50
    proxies:
"""

rule_providers_str = """
rule-providers:
  reject:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/reject.txt"
    path: ./ruleset/reject.yaml
    interval: 86400

  icloud:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/icloud.txt"
    path: ./ruleset/icloud.yaml
    interval: 86400

  apple:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/apple.txt"
    path: ./ruleset/apple.yaml
    interval: 86400

  google:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/google.txt"
    path: ./ruleset/google.yaml
    interval: 86400

  proxy:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/proxy.txt"
    path: ./ruleset/proxy.yaml
    interval: 86400

  direct:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/direct.txt"
    path: ./ruleset/direct.yaml
    interval: 86400

  private:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/private.txt"
    path: ./ruleset/private.yaml
    interval: 86400

  gfw:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/gfw.txt"
    path: ./ruleset/gfw.yaml
    interval: 86400

  tld-not-cn:
    type: http
    behavior: domain
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/tld-not-cn.txt"
    path: ./ruleset/tld-not-cn.yaml
    interval: 86400

  telegramcidr:
    type: http
    behavior: ipcidr
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/telegramcidr.txt"
    path: ./ruleset/telegramcidr.yaml
    interval: 86400

  cncidr:
    type: http
    behavior: ipcidr
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/cncidr.txt"
    path: ./ruleset/cncidr.yaml
    interval: 86400

  lancidr:
    type: http
    behavior: ipcidr
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/lancidr.txt"
    path: ./ruleset/lancidr.yaml
    interval: 86400

  applications:
    type: http
    behavior: classical
    url: "https://cdn.jsdelivr.net/gh/Loyalsoldier/clash-rules@release/applications.txt"
    path: ./ruleset/applications.yaml
    interval: 86400

rules:
  - RULE-SET,applications,DIRECT
  - DOMAIN,clash.razord.top,DIRECT
  - DOMAIN,yacd.haishan.me,DIRECT
  - RULE-SET,private,DIRECT
  - RULE-SET,reject,REJECT
  - RULE-SET,tld-not-cn,🚀 节点选择
  - RULE-SET,gfw,🚀 节点选择
  - RULE-SET,telegramcidr,🚀 节点选择
  - MATCH,DIRECT

# whitelist
# rules:
#   - RULE-SET,applications,DIRECT
#   - DOMAIN,clash.razord.top,DIRECT
#   - DOMAIN,yacd.haishan.me,DIRECT
#   - RULE-SET,private,DIRECT
#   - RULE-SET,reject,REJECT
#   - RULE-SET,icloud,DIRECT
#   - RULE-SET,apple,DIRECT
#   - RULE-SET,google,DIRECT
#   - RULE-SET,proxy,🚀 节点选择
#   - RULE-SET,direct,DIRECT
#   - RULE-SET,lancidr,DIRECT
#   - RULE-SET,cncidr,DIRECT
#   - RULE-SET,telegramcidr,🚀 节点选择
#   - GEOIP,LAN,DIRECT
#   - GEOIP,CN,DIRECT
#   - MATCH,🚀 节点选择

"""


def gen_rules_conf(snip, names):

    namestr = ""

    for name in names:
        namestr += f"      - {name}\n"

    fstr = str1+snip+proxy1+namestr+proxy2+namestr+rule_providers_str

    with open("ruleset-conf.yaml", "w", encoding="utf-8") as f:
        f.write(fstr)
