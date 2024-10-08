function Invoke-Subnetting {
    param([int]$MAGIC = 8)
    $mgk_net = @(); $nets = @(); $adrs = @(); $networks = @()
    for ($i = 1; $i -le $MAGIC; $i++) {
        $subList = @(); for ($j = 1; $j -le [Math]::Floor($MAGIC / 2); $j++) { $subList += "/$(($j * $MAGIC - $MAGIC + $i))" }
        $mgk_net += ,@($subList)
    }
    for ($i = 0; $i -lt $MAGIC; $i++) {
        $nets += [Math]::Pow(2, $i + 1); $adrs += [Math]::Pow(2, $MAGIC - $i - 1)
    }
    for ($i = 0; $i -lt $MAGIC; $i++) {
        $next_network = @()
        for ($j = 1; $j -le 10; $j++) {
            $step = $j * $adrs[$i]
            if ($step -lt 256) { $next_network += $step } else { break }
        }
        $networks += [PSCustomObject]@{
            index = $i + 1
            cidr = $("[" + ($mgk_net[$i] -join ", ") + "]")
            last_subnet = $MAGIC * [Math]::Floor($MAGIC * $MAGIC / 2) - $adrs[$i]
            nets = $nets[$i]
            addresses = $adrs[$i]
            range = "[1:$($adrs[$i] - 2)]"
            gateway = $adrs[$i] - 1
            next_network = $("[" + ($next_network -join ", ") + "]")
            network_calc = "$($adrs[$i])*(n<=$($nets[$i] - 1))"
        }
    }
    return $networks
}

function Invoke-TempHTML {
    param(
        [Parameter(ValueFromPipeline=$true)]
        [string]$HTMLContent
    )
    $tempFile = [System.IO.Path]::GetTempFileName() + ".html"
    $HTMLContent | Set-Content -Path $tempFile
    & start "$tempFile"
}

Invoke-Subnetting|ft
