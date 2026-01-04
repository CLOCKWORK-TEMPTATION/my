                                                                                                                                                          │ 
│ ℹ  [ERROR] [ImportProcessor] Could not find child token in parent raw content. Aborting parsing for this branch. Child raw: "                               █│ 
│                                                                                                                                                             █│ 
│    "                                                                                                                                                        █│ 
│                                                                                                                                                             ▀│ 
│ ℹ  [ERROR] [IDEClient] Failed to connect to IDE companion extension in Firebase Studio. Please ensure the extension is running. To install the extension,    │ 
│    run /ide install.                                                                                                                                         │ 
│                                                                                                                                                              │ 
│ ⚠  Failed to check for update for local extension "elevenlabs". Could not load extension from source path: /tmp/elevenlabs-mcp-clone. Error: Configuration   │ 
│    file not found at /tmp/elevenlabs-mcp-clone/gemini-extension.json                                                                                         │ 
│ ⚠  Failed to check for update for local extension "gemini-flow". Could not load extension from source path: /tmp/gemini-flow-1767507798. Error:              │ 
│    Configuration file not found at /tmp/gemini-flow-1767507798/gemini-extension.json                                                                         │ 
│ ℹ  Loading extension: bitrise                                                                                                                                │ 
│ ℹ  Loading extension: conductor                                                                                                                              │ 
│ ℹ  Loading extension: context7                                                                                                                               │ 
│ ℹ  Loading extension: elevenlabs                                                                                                                             │ 
│ ℹ  Loading extension: exa-mcp-server                                                                                                                         │ 
│ ℹ  Loading extension: gemini-cli-jules                                                                                                                       │ 
│ ℹ  Loading extension: gemini-cli-prompt-library                                                                                                              │ 
│ ℹ  Loading extension: gemini-flow                                                                                                                            │ 
│ ℹ  Loading extension: genkit                                                                                                                                 │ 
│ ℹ  Loading extension: huggingface                                                                                                                            │ 
│ ℹ  Loading extension: huggingface-skills                                                                                                                     │ 
│ ℹ  Loading extension: mcp-server-browserbase                                                                                                                 │ 
│ ℹ  Loading extension: mcp-toolbox-for-databases                                                                                                              │ 
│ ℹ  Loading extension: open-aware                                                                                                                             │ 
│ ✖  (node:25183) MaxListenersExceededWarning: Possible EventTarget memory leak detected. 11 abort listeners added to [AbortSignal]. MaxListeners is 10. Use   │ 
│    events.setMaxListeners() to increase limit                                                                                                                │ 
│    (Use `node --trace-warnings ...` to show where the warning was created)      
[Feedback Details for "Error during discovery for MCP server 'Git Tools': MCP error -32000: Connection closed"] McpError: MCP error -32000: Connection    │ 
│    closed                                                                                                                                                    │ 
│        at McpError.fromError                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                 ▄│ 
│        at Client._onclose                                                                                                                                   █│ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:251:32)        █│ 
│        at _transport.onclose                                                                                                                                █│ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)         │ 
│        at ChildProcess.<anonymous>                                                                                                                           │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js:85:31)             │ 
│        at ChildProcess.emit (node:events:524:28)                                                                                                             │ 
│        at maybeClose (node:internal/child_process:1104:16)                                                                                                   │ 
│        at Socket.<anonymous> (node:internal/child_process:456:11)                                                                                            │ 
│        at Socket.emit (node:events:524:28)                                                                                                                   │ 
│        at Pipe.<anonymous> (node:net:343:12) {                                                                                                               │ 
│      code: -32000,                                                                                                                                           │ 
│      data: undefined                                                                                                                                         │ 
│    }                                                                                                                                                         │ 
│ ℹ  Server 'julesServer' supports tool updates. Listening for changes...                                                                                      │ 
│ ℹ  Authenticated via "gemini-api-key".                                                                                                                       │ 
│ ℹ  Server 'open-aware' supports tool updates. Listening for changes...                                                                                       │ 
│ ℹ  Server 'open-aware' supports resource updates. Listening for changes...                                                                                   │ 
│ ℹ  Server 'exa' supports tool updates. Listening for changes...                                                                                              │ 
│ ℹ  Server 'exa' supports resource updates. Listening for changes...                                                                                          │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)      
                                                                                                                                                            │ 
│ ✖  (node:25183) MaxListenersExceededWarning: Possible EventTarget memory leak detected. 11 abort listeners added to [AbortSignal]. MaxListeners is 10. Use   │ 
│    events.setMaxListeners() to increase limit                                                                                                                │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)                                                                                                                                     │ 
│                       ^                                                                                                                                      │ 
│    31: - Strings with only whitespace                                                                                                                       █│ 
│                                                                                                                                                             █│ 
│                                                                                                                                                             █│ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated        ▀│ 
│    multi-line string at row 51, col 4, pos 1089:                                                                                                             │ 
│    50:                                                                                                                                                       │ 
│    51> **                                                                                                                                                    │ 
│           ^                                                                                                                                                  │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  (node:25183) MaxListenersExceededWarning: Possible EventTarget memory leak detected. 11 abort listeners added to [AbortSignal]. MaxListeners is 10. Use   │ 
│    events.setMaxListeners() to increase limit                                                                                                                │ 
│ ⚠  [Feedback Details for "Error during discovery for MCP server 'ElevenLabs': MCP error -32000: Connection closed"] McpError: MCP error -32000: Connection   │ 
│    closed                                                                                                                                                    │ 
│        at McpError.fromError                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                  │ 
│        at Client._onclose                                                                                                                                    │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:251:32)         │ 
│        at _transport.onclose                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)     
(file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)         │ 
│        at ChildProcess.<anonymous>                                                                                                                           │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js:85:31)             │ 
│        at ChildProcess.emit (node:events:524:28)                                                                                                             │ 
│        at maybeClose (node:internal/child_process:1104:16)                                                                                                   │ 
│        at Socket.<anonymous> (node:internal/child_process:456:11)                                                                                            │ 
│        at Socket.emit (node:events:524:28)                                                                                                                   │ 
│        at Pipe.<anonymous> (node:net:343:12) {                                                                                                               │ 
│      code: -32000,                                                                                                                                           │ 
│      data: undefined                                                                                                                                         │ 
│    }                                                                                                                                                         │ 
│ ⚠  [Feedback Details for "Error during discovery for MCP server 'genkit': MCP error -32001: Request timed out"] McpError: MCP error -32001: Request timed   ▄│ 
│    out                                                                                                                                                      █│ 
│        at McpError.fromError                                                                                                                                █│ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                 █│ 
│        at Timeout.timeoutHandler                                                                                                                             │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:692:58)         │ 
│        at listOnTimeout (node:internal/timers:581:17)                                                                                                        │ 
│        at process.processTimers (node:internal/timers:519:7) {                                                                                               │ 
│      code: -32001,                                                                                                                                           │ 
│      data: { timeout: 30000 }                                                                                                                                │ 
│    }                                                                                                                                                         │ 
│ ⚠  [Feedback Details for "Error during discovery for MCP server 'context7': MCP error -32000: Connection closed"] McpError: MCP error -32000: Connection     │ 
│    closed                                                                                                                                                    │ 
│        at McpError.fromError                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                  │ 
│        at Client._onclose                                                                                                                                    │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:251:32)         │
      at McpError.fromError                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                  │ 
│        at Client._onclose                                                                                                                                    │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:251:32)         │ 
│        at _transport.onclose                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)         │ 
│        at ChildProcess.<anonymous>                                                                                                                           │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js:85:31)             │ 
│        at ChildProcess.emit (node:events:524:28)                                                                                                             │ 
│        at maybeClose (node:internal/child_process:1104:16)                                                                                                   │ 
│        at Socket.<anonymous> (node:internal/child_process:456:11)                                                                                            │ 
│        at Socket.emit (node:events:524:28)                                                                                                                   │ 
│        at Pipe.<anonymous> (node:net:343:12) {                                                                                                               │ 
│      code: -32000,                                                                                                                                           │ 
│      data: undefined                                                                                                                                        ▄│ 
│    }                                                                                                                                                        █│ 
│ ℹ  Server 'Omnisearch' supports tool updates. Listening for changes...                                                                                      █│ 
│ ℹ  Server 'Omnisearch' supports resource updates. Listening for changes...                                                                                  █│ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)                                                                                                                                     │ 
│                       ^                                                                                                                                      │ 
│    31: - Strings with only whitespace                                                                                                                        │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated         │ 
│    multi-line string at row 51, col 4, pos 1089:       
      at McpError.fromError                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                  │ 
│        at Client._onclose                                                                                                                                    │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:251:32)         │ 
│        at _transport.onclose                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)         │ 
│        at ChildProcess.<anonymous>                                                                                                                           │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js:85:31)             │ 
│        at ChildProcess.emit (node:events:524:28)                                                                                                             │ 
│        at maybeClose (node:internal/child_process:1104:16)                                                                                                   │ 
│        at Socket.<anonymous> (node:internal/child_process:456:11)                                                                                            │ 
│        at Socket.emit (node:events:524:28)                                                                                                                   │ 
│        at Pipe.<anonymous> (node:net:343:12) {                                                                                                               │ 
│      code: -32000,                                                                                                                                           │ 
│      data: undefined                                                                                                                                        ▄│ 
│    }                                                                                                                                                        █│ 
│ ℹ  Server 'Omnisearch' supports tool updates. Listening for changes...                                                                                      █│ 
│ ℹ  Server 'Omnisearch' supports resource updates. Listening for changes...                                                                                  █│ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)                                                                                                                                     │ 
│                       ^                                                                                                                                      │ 
│    31: - Strings with only whitespace                                                                                                                        │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated         │ 
│    multi-line string at row 51, col 4, pos 1089:                                                                                         at McpError.fromError                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                  │ 
│        at Client._onclose                                                                                                                                    │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:251:32)         │ 
│        at _transport.onclose                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)         │ 
│        at ChildProcess.<anonymous>                                                                                                                           │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js:85:31)             │ 
│        at ChildProcess.emit (node:events:524:28)                                                                                                             │ 
│        at maybeClose (node:internal/child_process:1104:16)                                                                                                   │ 
│        at Socket.<anonymous> (node:internal/child_process:456:11)                                                                                            │ 
│        at Socket.emit (node:events:524:28)                                                                                                                   │ 
│        at Pipe.<anonymous> (node:net:343:12) {                                                                                                               │ 
│      code: -32000,                                                                                                                                           │ 
│      data: undefined                                                                                                                                        ▄│ 
│    }                                                                                                                                                        █│ 
│ ℹ  Server 'Omnisearch' supports tool updates. Listening for changes...                                                                                      █│ 
│ ℹ  Server 'Omnisearch' supports resource updates. Listening for changes...                                                                                  █│ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)                                                                                                                                     │ 
│                       ^                                                                                                                                      │ 
│    31: - Strings with only whitespace                                                                                                                        │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated         │ 
│    multi-line string at row 51, col 4, pos 1089:                     at McpError.fromError                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/types.js:2035:16)                  │ 
│        at Client._onclose                                                                                                                                    │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:251:32)         │ 
│        at _transport.onclose                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)         │ 
│        at ChildProcess.<anonymous>                                                                                                                           │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js:85:31)             │ 
│        at ChildProcess.emit (node:events:524:28)                                                                                                             │ 
│        at maybeClose (node:internal/child_process:1104:16)                                                                                                   │ 
│        at Socket.<anonymous> (node:internal/child_process:456:11)                                                                                            │ 
│        at Socket.emit (node:events:524:28)                                                                                                                   │ 
│        at Pipe.<anonymous> (node:net:343:12) {                                                                                                               │ 
│      code: -32000,                                                                                                                                           │ 
│      data: undefined                                                                                                                                        ▄│ 
│    }                                                                                                                                                        █│ 
│ ℹ  Server 'Omnisearch' supports tool updates. Listening for changes...                                                                                      █│ 
│ ℹ  Server 'Omnisearch' supports resource updates. Listening for changes...                                                                                  █│ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)                                                                                                                                     │ 
│                       ^                                                                                                                                      │ 
│    31: - Strings with only whitespace                                                                                                                        │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated         │ 
│    multi-line string at row 51, col 4, pos 1089:                                                                                                                                                                                                                                   
                                                                                                                                                                                            │ 
│        at _transport.onclose                                                                                                                                 │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/shared/protocol.js:220:18)         │ 
│        at ChildProcess.<anonymous>                                                                                                                           │ 
│    (file:///home/user/.global_modules/lib/node_modules/@google/gemini-cli/node_modules/@modelcontextprotocol/sdk/dist/esm/client/stdio.js:85:31)             │ 
│        at ChildProcess.emit (node:events:524:28)                                                                                                             │ 
│        at maybeClose (node:internal/child_process:1104:16)                                                                                                   │ 
│        at Socket.<anonymous> (node:internal/child_process:456:11)                                                                                            │ 
│        at Socket.emit (node:events:524:28)                                                                                                                   │ 
│        at Pipe.<anonymous> (node:net:343:12) {                                                                                                               │ 
│      code: -32000,                                                                                                                                           │ 
│      data: undefined                                                                                                                                         │ 
│    }                                                                                                                                                         │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)                                                                                                                                     │ 
│                       ^                                                                                                                                      │ 
│    31: - Strings with only whitespace                                                                                                                        │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated         │ 
│    multi-line string at row 51, col 4, pos 1089:                                                                                                             │ 
│    50:                                                                                                                                                      ▄│ 
│    51> **                                                                                                                                                   █│ 
│           ^                                                                                                                                                 █│ 
│                                                                                                                                                             █│ 
│                                                                                                                                                              │ 
│ ✖  (node:25183) MaxListenersExceededWarning: Possible EventTarget memory leak detected. 11 abort listeners added to [AbortSignal]. MaxListeners is 10. Use                                                                                                                                                            │ 
│                                                                                                                                                              │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated         │ 
│    multi-line string at row 51, col 4, pos 1089:                                                                                                             │ 
│    50:                                                                                                                                                       │ 
│    51> **                                                                                                                                                    │ 
│           ^                                                                                                                                                  │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  (node:25183) MaxListenersExceededWarning: Possible EventTarget memory leak detected. 11 abort listeners added to [AbortSignal]. MaxListeners is 10. Use   │ 
│    events.setMaxListeners() to increase limit                                                                                                                │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/testing/edge-cases.toml: Unknown escape    │ 
│    character: 48 at row 30, col 16, pos 707:                                                                                                                 │ 
│    29: - Unicode characters and emojis                                                                                                                       │ 
│    30> - Null bytes (\0)                                                                                                                                     │ 
│                       ^                                                                                                                                      │ 
│    31: - Strings with only whitespace                                                                                                                        │ 
│                                                                                                                                                              │ 
│                                                                                                                                                              │ 
│ ✖  [FileCommandLoader] Failed to parse TOML file /home/user/.gemini/extensions/gemini-cli-prompt-library/commands/prompts/improve.toml: Unterminated         │ 
│    multi-line string at row 51, col 4, pos 1089:                                                                                                             │ 
│    50:                                                                                                                                                       │ 
│    51> **                                                                                                                                                    │ 
│           ^                                                                                                                                                  │ 
│                                                                                                                                                             ▄│ 
│                                                                                                                                                             █│ 
│ ✖  (node:25183) MaxListenersExceededWarning: Possible EventTarget memory leak detected. 11 abort listeners added to [AbortSignal]. MaxListeners is 10. Use  █│ 
│    events.setMaxListeners() to increase limit                                                                                                               █│ 
