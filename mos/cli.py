import click
import os
import subprocess

@click.command()
@click.argument('infile', type=click.Path(exists=True, readable=True))
@click.argument('outfile', default="outfile.gif", type=click.Path(writable=True))
@click.option('--start', '-s', help='Start time in 00:00:00 format')
@click.option('--end', '-e', help='End time in 00:00:00 format')
@click.option('--scale', help='Scale factor. 0.5 to scale down by half', type=click.FLOAT)
@click.option('--dry-run', '-n', 'dryrun', is_flag=True, help='Construct the command and print it, but do not run it')
def cli(infile, outfile, start, end, scale, dryrun):
    """Simple program to make animated files such as GIFs using ffmpeg."""
    command_parts = [
        "ffmpeg",
        "-i",
        infile
    ]
    video_filters = ["format=rgb8,format=rgb24"]
    frame_rate = "-r 10"

    if start:
        command_parts.append(" ".join(["-ss", start]))
    if end:
        command_parts.append(" ".join(["-to", end]))

    # optional video filters
    if scale:
        video_filters.append("scale=iw*{multiplier}:-1".format(multiplier=scale))

    command_parts.append("-vf '{}'".format(",".join(video_filters)))
    command_parts.append(frame_rate)
    command_parts.append(outfile)

    command_str = " ".join(command_parts)

    # Echo info about what we are going to tell ffmpeg to do
    click.clear()
    click.echo(click.style('Attempting to run:', blink=True, bold=True))
    click.echo(click.style(command_str, fg='yellow'))

    if not dryrun:
        returncode = subprocess.call(command_str, shell=True)

        if returncode == 0:
            click.echo(click.style('Success!', bold=True, fg='green'))
        else:
            click.echo(click.style('Failure!', blink=True, bold=True, fg='red'))
